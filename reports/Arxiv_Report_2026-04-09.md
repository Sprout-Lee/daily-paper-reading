# Arxiv Daily Deep Report - 2026-04-09

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 4
---

## 1. EvoTSE: Evolving Enrollment for Target Speaker Extraction

**作者**: Zikai Liu, Ziqian Wang, Xingchen Li, Yike Zhu, Shuai Wang, Longshuai Xiao, Lei Xie
**链接**: [2604.06810](https://arxiv.org/abs/2604.06810)
**分类**: Audio Enhancement | **关键词**: Target Speaker Extraction, Speaker Confusion, Retrieval-Augmented Generation, Evolving Enrollment

# 论文总结：EvoTSE: Evolving Enrollment for Target Speaker Extraction

## 核心痛点
- **说话人混淆**：传统目标说话人提取（TSE）模型在干扰说话人声学特征类似时，错误提取干扰说话人。
- **静态注册限制**：固定注册无法处理目标说话人随时间变化的声学特征（如情感变化或语音努力变化），导致在长时长或域外（OOD）场景中性能下降。

## 方法创新
- **进化注册框架**：将静态TSE重新表述为进化管道，利用历史上下文动态更新注册，通过检索增强生成（RAG）机制从高置信度历史估计中检索相关注册。
- **关键组件**：包括上下文检索器（使用ECAPA-TDNN和Emotion2vec编码器进行双流检索）、骨干提取器、可靠性分类器（验证身份一致性）和内存策展人（管理内存库多样性）。
- **训练策略**：采用伪影感知的两阶段训练，提高对进化过程中伪影的鲁棒性。

## 实验结果
- 在多个基准测试中，EvoTSE实现了性能的持续改进，尤其是在OOD场景中，增强了模型的泛化能力。
- 实验表明，该方法减少说话人混淆，并放宽了对预录制注册音频的质量要求。

## 一句话评价
EvoTSE通过动态注册更新和检索机制，有效解决了TSE中的说话人混淆和静态注册问题，显著提升了在复杂音频场景下的提取性能。

---

## 2. DAT-CFTNet: Speech Enhancement for Cochlear Implant Recipients using Attention-based Dual-Path Recurrent Neural Network

**作者**: Nursadul Mamun, John H.L. Hansen
**链接**: [2604.06744](https://arxiv.org/abs/2604.06744)
**分类**: Speech Enhancement | **关键词**: Speech Enhancement, Cochlear Implant, Dual-path RNN, Attention Mechanism, Complex-valued Networks

# 论文详细总结

## 核心痛点
- Cochlear Implant (CI) 用户在嘈杂环境中面临严重听力挑战，其听力系统仅能恢复约10%的时频(T-F)内容，导致语音可懂度和质量下降。
- 传统语音增强(SE)方法在针对CI用户时效果有限，尤其在处理非平稳噪声和避免音乐伪影方面存在不足。

## 方法创新
- 提出DAT-CFTNet模型，结合修改后的复数频率转换网络(CFTNet)与双路径注意力循环神经网络(DAT-RNN)。
- DAT-RNN模块集成双路径RNN(DPRNN)和注意力机制，以优化时频区域的局部和全局上下文信息处理，精确区分语音和噪声。
- 引入变体模型，如DAT-CFTNet-F（优化频率块配置）和DAT-CFTNet-L（使用深度可分离卷积减少参数），以提升效率和适应性。

## 实验结果
- DAT-CFTNet在PESQ、STOI和SISDR等客观指标上优于基线模型（如CFTNet和DCCRN），尤其在低信噪比(SNR)下改进显著。
- 在多种噪声条件下（包括可见和未见噪声），模型均表现出稳定的性能提升，例如在平均SNR下，PESQ从2.31提高到2.39，STOI从92.33%提高到93.33%。
- 消融研究验证了注意力机制和模型变体的有效性，如DAT-CFTNet-F在SISDR上达到10.61 dB的改进。

## 一句话评价
该研究为CI用户设计了一个创新的语音增强模型，通过注意力机制和双路径RNN优化时频处理，显著提高了语音可懂度和质量，具有重要的应用潜力。

---

## 3. ULTRAS -- Unified Learning of Transformer Representations for Audio and Speech Signals

**作者**: Ameenudeen P E, Charumathi Narayanan, Sriram Ganapathy
**链接**: [2604.06702](https://arxiv.org/abs/2604.06702)
**分类**: Audio and Speech Representation Learning | **关键词**: Self-supervised Learning, Transformer, Audio Representation, Speech Representation, Time-Frequency Masking

# 核心痛点

自我监督学习（SSL）在语音处理中主要使用时间域预测目标（如 wav2vec 2.0、HuBERT），而音频表示学习通常在时频谱图上操作（如 SSAST）。这两种范式难以相互转移，导致模型在跨领域任务上性能下降，迫切需要统一的框架来联合学习音频和语音的表示。

# 方法创新

提出了 ULTRAS（Unified Learning of Transformer Representations for Audio and Speech），一个基于变换器的统一框架。关键创新包括：1) 对长时间段音频（160ms 窗口）进行掩码，以编码音节级声学信息；2) 将输入音频转换为 log-mel 频谱图，并分割为频谱块进行编码；3) 使用组合损失函数（加权时间损失和频谱损失）联合预测频谱目标（通过 K-means 量化）和时间目标（基于 HuBERT 嵌入），迫使表示编码时频特征；4) 架构借鉴 Vision Transformer，采用随机掩码策略和变换器编码器。

# 实验结果

在多种语音和音频下游任务（如语音识别、音频事件分类）上进行了评估，使用冻结的 SSL 模型和轻量级分类头。预训练在 LibriSpeech 和 AudioSet 的混合数据集上进行（200 小时和 2000 小时设置）。实验结果显示，ULTRAS 在性能上优于其他基线方法（如 wav2vec 2.0、HuBERT 和 SSAST），验证了联合时频建模的有效性。

# 一句话评价

ULTRAS 是一个创新的统一框架，通过联合预测时频目标，显著提升了音频和语音表示学习的泛化能力和下游任务性能。

---

## 4. Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment

**作者**: Asif Azad, MD Sadik Hossain Shanto, Mohammad Sadat Hossain, Bdour Alwuqaysi, Sabri Boughorbel, Yahya Bokhari, Abdulrhman Aljouie, Ayah Othman Sindi, Ehsan Hoque
**链接**: [2604.06191](https://arxiv.org/abs/2604.06191)
**分类**: Speech Recognition | **关键词**: Arabic phoneme recognition, speech assessment, clinical validation, automated speech therapy, phoneme-level scoring

## 核心痛点
阿拉伯语（现代标准阿拉伯语MSA）缺乏临床验证的自动化音素级发音评估工具，现有专有系统如Microsoft Azure Pronunciation Assessment未针对阿拉伯语音系学特点（如丰富辅音库、咽音音素）进行本地化，临床有效性和可扩展性受限。

## 方法创新
提出Harf-Speech框架：一个模块化系统，用于阿拉伯语音素级发音评估。方法包括：1. 使用MSA音标化器生成参考音素序列；2. 微调多个ASR架构（如OmniASR-CTC-1B-v2）进行语音到音素预测；3. 基于Levenshtein对齐和最长公共子序列（LCS）算法进行音素分割和评分；4. 混合评分器结合准确性和完整性指标，输出临床尺度的分数。

## 实验结果
- 音素错误率（PER）：微调模型OmniASR-CTC-1B-v2在阿拉伯语音素数据上达到8.92% PER，优于零样本多模态模型（如Gemini-3-pro的15.07% PER）。
- 临床验证：由三名认证语音语言病理学家独立评分40个话语，Harf-Speech与专家平均分数的Pearson相关系数为0.791，ICC(2,1)为0.659，超越现有端到端评估框架。
- 实时性能：OmniASR-CTC-1B-v2具有低实时因子（RTF 0.004），适合实际部署。

## 一句话评价
Harf-Speech提供了一个开放、模块化、临床对齐的阿拉伯语音素级发音评估框架，通过本地化建模和专家验证，推动了可扩展语音治疗和语言学习的技术进步。

---

