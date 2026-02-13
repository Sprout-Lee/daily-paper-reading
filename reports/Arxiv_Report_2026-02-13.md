# Arxiv Daily Deep Report - 2026-02-13

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 5
---

## 1. Exploring Frequency-Domain Feature Modeling for HRTF Magnitude Upsampling

**作者**: Xingyu Chen, Hanwen Bi, Fei Ma, Sipei Zhao, Eva Cheng, Ian S. Burnett
**链接**: [2602.11670](https://arxiv.org/abs/2602.11670)
**分类**: Audio Enhancement | **关键词**: HRTF, magnitude upsampling, frequency-domain modeling, Conformer, sparse measurements

# 核心痛点
传统 HRTF 上采样方法（如距离加权插值和基础函数分解）依赖于单个主题的稀疏测量，受空间采样定理限制，在稀疏采样条件下性能显著下降。现有学习型方法虽利用跨主题信息，但大多聚焦于空间关系建模，频域依赖关系被隐式或独立处理，未能充分利用 HRTF 幅度响应在频域的局部连续性和长程结构。

# 方法创新
论文系统调查频域特征建模，比较不同架构（包括每频率多层感知器、卷积、膨胀卷积和注意力模型）在 HRTF 幅度上采样中的效果。基于分析，提出频域 Conformer 架构（FD-Conformer），结合 Conformer 设计以显式联合捕捉局部频谱连续性和长程频率相关性，改善频域依赖建模。

# 实验结果
在 SONICOM 和 HUTUBS 数据集上的实验表明，所提方法在 interaural level difference (ILD) 和 log-spectral distortion (LSD) 指标上达到最先进性能，特别是在严重稀疏测量条件下重建准确性更高，验证了显式频域建模的有效性。

# 一句话评价
该研究通过创新性频域建模，显著提升了稀疏测量下的 HRTF 幅度上采样精度，推动了空间音频渲染技术的发展。

---

## 2. TC-BiMamba: Trans-Chunk bidirectionally within BiMamba for unified streaming and non-streaming ASR

**作者**: Qingshun She, Jing Peng, Yangui Fang, Yu Xi, Kai Yu
**链接**: [2602.11546](https://arxiv.org/abs/2602.11546)
**分类**: Speech Recognition | **关键词**: Speech Recognition, Bidirectional Mamba, Dynamic Chunk

## 核心痛点
现有基于双向Mamba（BiMamba）的流式自动语音识别（ASR）方法在动态块大小训练时面临高开销问题，传统块处理（chunk-wise processing）导致训练速度慢、内存使用高和性能下降，且现有方法如LC-BiMamba限于固定块大小解码。

## 方法创新
本论文提出TC-BiMamba模型，结合双向Mamba和CNN编码器，核心创新是Trans-Chunk机制，使BiMamba在动态块大小下以离线风格训练双向序列，有效捕获全局上下文。该方法通过简化训练过程，实现1.3倍训练速度提升、50%内存减少和性能改善，并使用混合解码器（Mamba替换自注意力）维持线性计算复杂度。

## 实验结果
在AISHELL-1和AISHELL-2数据集上实验，TC-BiMamba在离线和非流式ASR（如块大小16设置）中表现优异。与基线U2++相比，字符错误率（CER）降低，如离线CTC CER为5.25%（AISHELL-1），与LC-BiMamba匹配但模型参数更少（约47M参数）。训练效率提升验证了Trans-Chunk机制的有效性。

## 一句话评价
这是一项创新的工作，通过Trans-Chunk机制高效解决了动态块大小训练挑战，推动了流式ASR的统一模型发展，具有实际应用价值。

---

## 3. SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis

**作者**: Yifan Liang, Andong Li, Kang Yang, Guochen Yu, Fangkun Liu, Lingling Dai, Xiaodong Li, Chengshi Zheng
**链接**: [2602.11477](https://arxiv.org/abs/2602.11477)
**分类**: Lip-to-Speech Synthesis | **关键词**: Lip-to-Speech Synthesis, Latent Diffusion Models, Neural Audio Codec, Flow Matching, Hierarchical Subspace

## 核心痛点

当前唇语到语音合成（L2S）方法通常依赖于中间表示，如mel频谱图或离散自监督学习（SSL）令牌，导致信息损失，无法捕捉高保真语音所需的细粒度声学细节。视觉到音频的映射是ill-posed问题，一个唇动序列对应多个有效语音渲染，增加了合成难度。现有方法如Uni-Dubbing使用离散令牌预测，但视觉输入信息稀疏，难以支持复杂的语言建模任务。

## 方法创新

本文提出SLD-L2S框架，基于层次子空间潜在扩散模型。创新点包括：直接映射视觉唇动到预训练神经音频编解码器的连续潜在空间，避免中间表示的信息损失；设计子空间分解模块将视觉表示分解到多个并行子空间；引入扩散卷积块（DiCB）作为网络骨干，捕获时间和跨子空间依赖；采用重新参数化流匹配技术直接生成目标潜在向量，并结合语义一致性损失和语音语言模型（SLM）损失以提高训练效果和语音清晰度。

## 实验结果

实验表明，SLD-L2S在多个基准数据集上实现了最先进的生成质量，在客观和主观评估中均超越现有方法。

## 一句话评价

SLD-L2S通过创新地集成层次子空间潜在扩散模型和音频编解码器，为唇语到语音合成提供了高保真、高效的解决方案。

---

## 4. Musical Metamerism with Time--Frequency Scattering

**作者**: Vincent Lostanlen, Han Han
**链接**: [2602.11896](https://arxiv.org/abs/2602.11896)
**分类**: Music Cognition | **关键词**: audio texture synthesis, automatic differentiation, joint time–frequency scattering, music cognition

## 核心痛点
音乐认知研究中缺乏合适的‘最小对’刺激来精确测量轮廓组件（如旋律、节奏、音色）在音乐熟悉性中的相对权重。人类能基于整体轮廓识别音乐，但现有方法难以解释这种认知过程，且音乐记忆不依赖于时频域中的固定模式，导致实验设计挑战。

## 方法创新
提出基于联合时频散射（JTFS）的方法生成‘音乐共色’。JTFS 通过两个阶段：首先使用 Morlet 小波滤波器组提取听觉特征，然后使用时频调制小波分析谱图。通过高斯低通滤波实现时间平移（尺度 T）和频率平移（尺度 F）的不变性，从而捕捉音乐轮廓。使用 Kymatio 开源软件（支持 GPU 计算和自动微分）实现，无需手动预处理如转录或源分离。重建过程采用梯度下降，从噪声信号优化生成与原始音频感知相似的 metamers。

## 实验结果
论文片段未提供具体实验数据或定量结果，但详细描述了方法的数学基础、算法实现和代码示例，表明该方法能有效生成音乐共色，适用于音乐认知实验的刺激设计，并具有计算效率。

## 一句话评价
该研究创新性地将 JTFS 应用于音乐共色生成，为音乐认知研究提供了无需预处理的自动化工具，具有促进实验设计和音频合成的潜力。

---

## 5. When Audio-LLMs Don't Listen: A Cross-Linguistic Study of Modality Arbitration

**作者**: Jayadev Billa
**链接**: [2602.11488](https://arxiv.org/abs/2602.11488)
**分类**: Audio-Language Models | **关键词**: Audio-LLMs, Modality Arbitration, Text Dominance, Cross-Linguistic Study, ALME Benchmark

## 核心痛点
音频-语言模型（Audio-LLMs）在处理音频和文本冲突时，系统性倾向于遵循文本而非音频，即使被明确指示信任音频。这被称为文本主导（text dominance），揭示了模型在模态仲裁中的不对称性，可能导致实际部署中错误依赖陈旧或不正确的文本信息，影响语音接口的可靠性。

## 方法创新
论文引入音频-LLM模态评估（ALME）基准，包含57,602个控制的音频-文本冲突刺激，跨8种语言（如英语、中文、日语等）。通过文本主导比率（TDR）量化模型行为，并比较音频-文本冲突与文本-文本冲突以隔离模态特定效应。方法包括细粒度调整消融实验（如训练音频投影层或应用LoRA）来定位文本主导的来源，以及使用级联基线区分信息内容和仲裁可访问性。

## 实验结果
关键发现：音频-LLMs在音频-文本冲突下的文本主导（TDR=16.6%）比文本-文本冲突（TDR=1.6%）高10倍，表明仲裁不对称性；音频嵌入的信息内容更高（音频-仅准确性97.2% vs 级联准确性93.9%），但文本更易于仲裁访问。干预措施显示：强制转录增加文本主导（从19%到33%），而将文本框架为“故意损坏”减少80%文本主导；跨语言和跨模型（如GPT-4o、Gemini 2.0 Flash、Qwen2-Audio、Ultravox）存在显著变异，CJK/阿拉伯语模型通常文本主导更高。细粒度调整消融提供因果证据：文本主导源于LLM推理而非音频编码器。

## 一句话评价
论文通过多语言、多模型实验系统性地揭示了音频-LLMs在模态仲裁中的偏差，为改进模型设计和评估提供了重要见解，强调了信息内容与仲裁可访问性的关键区别。

---

