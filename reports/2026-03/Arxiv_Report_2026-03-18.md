# Arxiv Daily Deep Report - 2026-03-18

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 7
---

## 1. HRTF-guided Binaural Target Speaker Extraction with Real-World Validation

**作者**: Yoav Ellinson, Sharon Gannot
**链接**: [2603.16668](https://arxiv.org/abs/2603.16668)
**分类**: Audio Enhancement | **关键词**: Binaural audio, Target Speaker Extraction, HRTF

**核心痛点**  
传统目标说话者提取（TSE）方法在双耳音频设置中依赖于到达方向（DOA）估计或注册信号，可能扭曲感知的空间位置，影响语音可懂度和听感，尤其对听力受损听众不利。鸡尾酒会问题在混响和并发说话者环境下更具挑战性。

**方法创新**  
提出一种基于头部相关传递函数（HRTF）的双耳TSE框架，使用HRTF作为显式空间先验来指导提取。模型基于多通道深度盲源分离骨干，适应双耳设置，训练在多样化的测量HRTF数据上以实现跨听众泛化，而非针对特定听众。通过HRTF调制特征，保留双耳线索（如ILD和ITD），同时增强语音质量。架构包括卷积编码器、NBC2自注意力块和线性解码器，操作在STFT域。

**实验结果**  
使用WSJ0语料库和SofaMyRoom框架模拟混响环境（T60在0.2-0.8秒，SIR在-5到5 dB）。损失函数结合尺度不变信噪比（SI-SDR）和平均绝对误差（MAE）。验证通过模拟和真实头躯模拟器（HATS）记录，显示在保留空间一致性的同时提高了语音质量。

**一句话评价**  
该工作创新地利用HRTF作为空间线索，有效解决双耳TSE中的空间保留问题，具有跨听众泛化能力和实际应用潜力。

---

## 2. Speakers Localization Using Batch EM In Unfolding Neural Network

**作者**: Rina Veler, Sharon Gannot
**链接**: [2603.16278](https://arxiv.org/abs/2603.16278)
**分类**: Sound Source Localization | **关键词**: Sound source localization, Unfolding neural network, Expectation Maximization, Pair-wise relative phase ratio

# 核心痛点
传统声音源定位方法（如 SRP-PHAT、MUSIC、MLE）在真实环境中（如混响和噪声）表现不佳，特别是对于多声源。数据驱动的深度学习网络（DNN）缺乏可解释性，而经典迭代算法则更透明，但可能对初始化和局部最优敏感。

# 方法创新
提出了一种可解释的展开期望最大化网络（Unfolded EM Network），通过将迭代 EM 过程嵌入到编码器-EM-解码器架构中，减少了初始化敏感性并改进了收敛性。使用 Pair-Wise Relative Phase Ratios（PRPs）作为特征，基于复杂高斯混合模型（CGMM）进行最大似然估计，并引入离群聚类增强鲁棒性。

# 实验结果
在合成数据集上（基于 WSJ 语料库）进行实验，对比 Batch-EM 基线。结果显示，在混响条件下（T60=0.2s），提议的网络将 RMSE 降低了约 39%，并显著减少了定位误差超过 0.5 米的样本比例，表现出优越的准确性和鲁棒性。

# 一句话评价
该网络在混响环境中显著提高了定位鲁棒性，有效结合了数据驱动方法的性能和经典算法的可解释性。

---

## 3. Robust Generative Audio Quality Assessment: Disentangling Quality from Spurious Correlations

**作者**: Kuan-Tang Huang, Chien-Chun Wang, Cheng-Yeh Yang, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen
**链接**: [2603.16201](https://arxiv.org/abs/2603.16201)
**分类**: Audio Quality Assessment | **关键词**: audio quality assessment, mean opinion score, domain adversarial training, robust generalization

### 核心痛点
数据稀缺导致自动平均意见分数（MOS）预测模型容易学习虚假相关性，如数据集特定的声学特征（如乐器音色、环境背景噪声），而不是泛化的质量特征，从而在部署到未见数据时泛化能力差。

### 方法创新
引入领域对抗训练（DAT）框架，通过梯度反转层（GRL）强制模型学习领域不变的表示，以分离质量感知和干扰因素。系统研究三种领域定义策略：DAT-Source（基于数据集元数据）、DAT-Kmeans（基于K-means聚类的隐式声学模式）和DAT-Random（随机分配作为基线），并强调策略选择依赖于特定MOS方面（如生产质量、内容享受）。

### 实验结果
在AES-Natural数据集上评估，涵盖四个MOS维度：生产质量（PQ）、生产复杂性（PC）、内容享受（CE）和内容有用性（CU）。实验表明，DAT策略有效减轻声学偏差，提高与人类评分的相关性（如皮尔逊相关系数），并在未见生成音频场景中实现卓越泛化，优于静态领域先验方法。使用MultiGauss和Audiobox-Aesthetics作为骨干模型验证了鲁棒性。

### 一句话评价
该研究通过创新的领域对抗训练和系统化的领域定义探索，为生成音频质量评估提供了更可靠、泛化的解决方案，解决了数据稀缺下的虚假相关性问题。

---

## 4. AILive Mixer: A Deep Learning based Zero Latency Automatic Music Mixer for Live Music Performances

**作者**: Devansh Zurale, Iris Lorente, Michael Lester, Alex Mitchell
**链接**: [2603.15995](https://arxiv.org/abs/2603.15995)
**分类**: Automatic Music Mixing | **关键词**: Automatic music mixing, Zero latency, Deep learning

**核心痛点**：现场音乐表演中，多轨音频常受到声道间声学泄漏（bleeds）的污染，且需要零延迟混音以保持音频-视频同步。现有自动音乐混音（AMM）系统大多针对离线生产，缺乏处理泄漏和实现零延迟的端到端解决方案。

**方法创新**：提出了AiLive Mixer（ALM），一个基于深度学习的系统。主要创新包括：1) 多率处理（MR），将系统分为两个帧率（如975ms和50ms）以降低延迟；2) 架构改进，如Transformer encoder块学习声道间上下文，GRU块学习时间上下文；3) 数据增强策略，通过参数化工具模拟泄漏；4) 零延迟训练，预测未来音频帧的增益。系统基于DMC（Differentiable Mixing Console）改进，增加了RMS条件、音频嵌入模型微调等功能。

**实验结果**：论文在Section 6展示了实验结果，比较了多率处理和单率处理（SR），并在真实现场表演数据上测试。结果表明，ALM能有效处理泄漏，实现零延迟混音，并在延迟和混音质量上优于基线方法。

**一句话评价**：ALM是首个针对现场音乐表演的端到端深度学习自动混音系统，创新性地解决了泄漏和延迟问题，为现场音频处理提供了新方向。

---

## 5. Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech

**作者**: Jaesung Bae, Xiuwen Zheng, Minje Kim, Chang D. Yoo, Mark Hasegawa-Johnson
**链接**: [2603.15988](https://arxiv.org/abs/2603.15988)
**分类**: Speech Quality Assessment | **关键词**: dysarthria, speech quality assessment, data augmentation

# 核心痛点
DSQA（构音障碍语音质量评估）面临数据稀缺问题，依赖昂贵的主观专家评估，且现有模型（如SpICE）在跨语言和病因的未见数据集上鲁棒性不足，限制了临床应用和泛化能力。

# 方法创新
论文提出一个三阶段框架：首先，使用基于Whisper的教师模型为SAP数据集中未标记的样本生成伪标签；其次，结合LibriSpeech正常语音数据集，进行弱监督预训练，采用标签感知对比学习策略以增强对多样说话人和声学条件的鲁棒性；最后，微调预训练模型用于下游DSQA回归任务，以实现严重性级别估计。该方法通过伪标签和数据增强，有效利用未标记数据和大规模正常语音，提升模型性能。

# 实验结果
在五个跨域测试数据集（UASpeech、DysArinVox、EasyCall、EWA-DB、NeuroVoz）上，平均SRCC（Spearman秩相关系数）达到0.761，优于基于Whisper的基线（平均SRCC 0.732）和SOTA方法如SpICE。在SAP测试集上，SRCC为0.719。实验表明，弱监督和LibriSpeech集成对提升跨域鲁棒性至关重要。

# 一句话评价
该研究通过创新数据增强和弱监督对比学习框架，成功解决了DSQA中的数据稀缺挑战，显著提高了模型在多样未见数据集上的鲁棒性和性能。

---

## 6. RECOVER: Robust Entity Correction via agentic Orchestration of hypothesis Variants for Evidence-based Recovery

**作者**: Abhishek Kumar, Aashraya Sachdeva
**链接**: [2603.16411](https://arxiv.org/abs/2603.16411)
**分类**: Speech Recognition | **关键词**: entity correction, agentic AI, multi-hypothesis fusion

# 核心痛点
- 自动语音识别（ASR）在罕见和领域特定实体（如金融、医学术语）上表现不佳，错误成本高。
- 如果实体在 ASR 输出中完全缺失或严重损坏，后处理校正困难，传统方法证据有限。
- 大型语言模型（LLM）用于校正时容易产生幻觉或过度校正，缺乏严格约束。

# 方法创新
- 提出 RECOVER 框架：一个代理性校正框架，通过协调多假设作为证据进行实体恢复。
- 利用温度采样从单一 ASR 模型（Whisper-small）生成多个假设，以捕获互补错误。
- 四种校正策略：1-Best（单假设）、Entity-Aware Select（基于实体匹配选择）、ROVER Ensemble（多数投票合并）、LLM-Select（LLM 驱动选择），共享代理工具管道。
- 代理架构包括三个工具：Fuse Hypotheses（融合假设）、Propose Corrections（LLM 提议编辑）、Verify & Apply（验证并应用），并施加约束（如替换必须来自实体列表）。

# 实验结果
- 在五个多样数据集（Earnings-21、ATCO2、Eka-Medical、Common Voice、ContextASR-Bench）上评估。
- 实体短语词错误率（E-WER）相对降低 8-46%，召回率提高高达 22 个百分点。
- LLM-Select 策略在实体校正中表现最佳，同时保持整体 WER。

# 一句话评价
RECOVER 是一个鲁棒的后处理框架，通过代理性协调多假设和约束性 LLM 编辑，显著提升 ASR 实体校正的准确性和鲁棒性。

---

## 7. CAST-TTS: A Simple Cross-Attention Framework for Unified Timbre Control in TTS

**作者**: Zihao Zheng, Wen Wu, Chao Zhang, Mengyue Wu, Xuenan Xu
**链接**: [2603.16280](https://arxiv.org/abs/2603.16280)
**分类**: Text-to-Speech | **关键词**: Text-to-Speech, Timbre Control, Cross-Attention

# 核心痛点
当前TTS系统通常为语音提示和文本提示的音色控制使用单独模型，统一这两种控制信号到一个模型是理想的，但跨模态对齐的挑战导致架构和训练目标过于复杂。

# 方法创新
提出CAST-TTS框架：使用预训练编码器（Flan-T5用于文本、WavLM-based ECAPA-TDNN用于语音）提取特征，通过多阶段训练策略在共享嵌入空间中对齐语音和投影的文本表示，并利用单一的跨注意力机制统一控制音色，简化了架构。

# 实验结果
在语音提示任务中，CAST-TTS达到最高SPK-SIM（78.4），并在WER（2.05%）和UTMOS（3.91）等指标中具有竞争力；在文本提示任务中，相比基线方法（如CapSpeech-NAR和Parler-TTS），CAST-TTS在Style-ACC（91.15%）和主观评估（如Sim-MOS 4.11）上表现更优，整体性能与专用单输入模型相当。

# 一句话评价
CAST-TTS是一个简单有效的框架，通过统一的跨注意力机制简化了音色控制的跨模态对齐，在保持高性能的同时提高了灵活性。

---

