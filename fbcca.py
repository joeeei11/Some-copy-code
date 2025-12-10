# -*- coding: utf-8 -*-

from sklearn.cross_decomposition import CCA
from filterbank import filterbank
from scipy.stats import pearsonr
import numpy as np


# 输入：list_Freqs, fs, num_smpls, nHarms

def cca_reference(list_freqs, fs, num_smpls, num_harms=3):  # 刺激频率列表；采样率；样本数；谐波数
    num_freqs = len(list_freqs)
    tidx = np.arange(1, num_smpls + 1) / fs  # 每次试验时间

    y_ref = np.zeros((num_freqs, 2 * num_harms, num_smpls))
    for freq_i in range(num_freqs):
        tmp = []
        for harm_i in range(1, num_harms + 1):
            stim_freq = list_freqs[freq_i]
            tmp.extend([np.sin(2 * np.pi * tidx * harm_i * stim_freq),
                        np.cos(2 * np.pi * tidx * harm_i * stim_freq)])
        y_ref[freq_i] = tmp  # 谐波数*2 产生sin-cos参考信号

    return y_ref  # 参考信号：目标数量, 通道数量*2, 数据长度

# 输入：data, list_freqs, fs, num_harms, num_fbs

def fbcca(data, list_freqs, fs, num_harms=3, num_fbs=5):  # data: 目标数量, 通道数量, 数据长度
    # print('fbcca data shape:{}'.format(data.shape))
    fb_coefs = np.power(np.arange(1, num_fbs + 1), (-1.25)) + 0.25  # 加权函数 wn = n^(-a)+b

    num_targs = len(list_freqs)
    _, num_smpls = data.shape

    y_ref = cca_reference(list_freqs, fs, num_smpls, num_harms)
    cca = CCA(n_components=1)  # 初始化 CCA

    # 结果矩阵
    r = np.zeros((num_fbs, num_targs))

    for fb_i in range(num_fbs):  # 处理不同滤波器组
        testdata = filterbank(data, fs, fb_i)  # 滤波器组过滤后的数据
        for class_i in range(num_targs):   # 刺激频率表
            refdata = np.squeeze(y_ref[class_i, :, :])  # 挑选相应的频率目标参考信号
            test_C, ref_C = cca.fit_transform(testdata.T, refdata.T)  # 先拟合，后标准化
            #  每个观测值的变量
            #  行数应该相同，所以在这里转置
            #  输出两组最高相关线性组合
            r_tmp, _ = pearsonr(np.squeeze(test_C), np.squeeze(ref_C))  # 皮尔森相关系数，输出 r：相关系数[-1, 1] ; p:p越小，相关系数越显著
            if r_tmp == np.nan:
                r_tmp = 0
            r[fb_i, class_i] = r_tmp

    rho = np.dot(fb_coefs, r)  # 所有不同滤波器组结果的r的加权和
    print(rho)  # 输出相关性
    result = np.argmax(rho)  # 从目标中获取最大值作为最终预测值(获取索引)，而索引表示最大条目(最可能的目标)
    THRESHOLD = 0.1   # 阈值
    if abs(rho[result]) < THRESHOLD:  # 2.587=np.sum(fb_coefs*0.8) #2.91=np.sum(fb_coefs*0.9) #1.941=np.sum(fb_coefs*0.6)
        return 999  # 如果相关性不够大，就不返回任何命令
    else:
        return result
