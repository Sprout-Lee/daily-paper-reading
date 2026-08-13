# Arxiv Daily Deep Report - 2026-02-19

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 9
---

## 1. SELEBI: Percussion-aware Time Stretching via Selective Magnitude Spectrogram Compression by Nonstationary Gabor Transform

**作者**: Natsuki Akaishi, Nicki Holighaus, Kohei Yatabe
**链接**: [2602.16421](https://arxiv.org/abs/2602.16421)
**分类**: Audio Enhancement | **关键词**: Phase vocoder, Time stretching, Percussion smearing, Nonstationary Gabor Transform, SELEBI

## 核心痛点
相位声码器（PV）基的时间伸缩技术在音频信号处理中被广泛应用，但在处理打击乐成分时会出现'percussion smearing'（打击乐模糊）的artifact。这是由于幅度谱在时间伸缩过程中被拉长，而新生成的相位却是局部化的，导致时域结构不匹配，从而严重降低打击乐部分的质量。传统方法要么依赖启发式处理，要么进行信号分离，但都存在局限性，无法完全消除该问题。

## 方法创新
本文提出SELEBI方法，利用非平稳Gabor变换（NSDGT）实现自适应时间-频率分析。核心创新是动态调整分析窗口长度：在含有显著打击乐能量的区域使用短窗口，直接计算时间局部化的幅度谱。这样做确保了幅度和相位谱在时域结构上的一致性，同时保留了完美重构属性，使得合成信号稳定且高保真。该方法避免了信号分离，专注于解决幅度与相位的不匹配问题，提供了理论上的严谨性。

## 实验结果
实验结果表明，SELEBI方法能有效减轻打击乐模糊，并在不同拉伸因子下产生自然的音质。相比传统相位声码器和现有打击乐感知方法，SELEBI在保持音频特征（如清晰度和动态范围）方面表现更优。

## 一句话评价
SELEBI通过自适应窗口压缩和数学严格的处理，成功解决了时间伸缩中的打击乐模糊问题，为音频处理提供了高效且稳定的新方案。

---

## 2. Online Single-Channel Audio-Based Sound Speed Estimation for Robust Multi-Channel Audio Control

**作者**: Andreas Jonas Fuglsig, Mads Græsbøll Christensen, Jesper Rindom Jensen
**链接**: [2602.16416](https://arxiv.org/abs/2602.16416)
**分类**: Audio Control | **关键词**: Audio-Based, Sound Speed Estimation, Single-Channel

核心痛点：空间音频控制（如声区控制、主动噪声控制）依赖于准确的声学传播模型，但环境变化（特别是声速变化）会导致声学脉冲响应的系统性延迟和相位不匹配，从而降低性能。现有方法通常假设已知声速、需要多个麦克风或依赖离线校准，不适用于传感器配置有限的系统。

方法创新：提出一种在线单通道声速估计方法，仅需一个观察麦克风在多通道音频播放期间运行。该方法利用SICER（Sinc Interpolation–Compression/Expansion Resampling）模型来描述声速变化对信号的影响，通过最小化测量音频信号与参数声学模型预测之间的误差来估计当前声速。算法框架包括信号建模、声速估计和鲁棒控制，允许在声速变化超出阈值时更新控制滤波器。

实验结果：仿真实验在室内设置（16个扬声器、多控制麦克风）中进行，声速在333m/s到353m/s间变化。结果显示，该方法能准确跟踪声速变化，对白噪声、语音和音乐等多种输入信号均有效。在声区控制应用中，使用估计声速补偿传播误差后，声学对比度（AC）提高、归一化信号失真功率（nSDP）降低，性能优于固定滤波器基准，接近基于真实声速的基线。

一句话评价：该论文通过创新性的在线单通道声速估计技术，为多通道音频控制系统提供了实用的鲁棒性增强方案。

---

## 3. Multi-Channel Replay Speech Detection using Acoustic Maps

**作者**: Michael Neri, Tuomas Virtanen
**链接**: [2602.16399](https://arxiv.org/abs/2602.16399)
**分类**: Speech Anti-Spoofing | **关键词**: Replay attack detection, Acoustic maps, Multi-channel audio

# 核心痛点
自动说话人验证系统在实时语音助手中对重放攻击高度脆弱，现有方法难以可靠区分真实语音和重放语音，尤其是在多通道录音中缺乏有效的空间特征表示。

# 方法创新
提出声学地图作为新颖的空间特征表示，通过基于延迟和求和波束形成的经典方法计算，编码方向能量分布以捕捉人类语音辐射和扬声器重放之间的物理差异。设计轻量级卷积神经网络（约6k参数）对声学地图进行分类，实现高效检测。

# 实验结果
在ReMASC数据集上表现出竞争性性能，模型在环境依赖和独立条件下均保持鲁棒性，能泛化到不同麦克风阵列、波束形成器和未见过的声学环境。

# 一句话评价
该方法利用声学地图提供了一种紧凑、物理可解释的特征空间，有效提升了多通道重放语音检测的准确性和泛化能力。

---

## 4. Color-based Emotion Representation for Speech Emotion Recognition

**作者**: Ryotaro Nagase, Ryoichi Takashima, Yoichi Yamashita
**链接**: [2602.16256](https://arxiv.org/abs/2602.16256)
**分类**: Speech Emotion Recognition | **关键词**: speech emotion recognition, color attribute regression, machine learning, deep learning, multitask learning

## 核心痛点
传统语音情感识别方法主要依赖分类标签（如快乐、愤怒）或维度标签（如效价、唤醒度），但这些方法在表示情感的多样性和可解释性方面存在局限：分类方法无法处理混合或模糊情感，维度方法虽连续但不易直观理解。

## 方法创新
论文提出基于颜色属性（色调、饱和度、值）的情感表示框架，作为连续且直观的情感分数。通过众包标注日本情感语音语料库（JVNV），分析颜色属性与情感的关系。构建了支持向量回归和深度神经网络模型进行颜色属性预测，并探索多任务学习，结合颜色属性回归和情感分类以提升性能。

## 实验结果
实验表明，颜色属性与情感类别显著相关：例如，快乐和惊讶的色调集中在45度附近（黄色系），愤怒在340度（红色系），负面情绪如恐惧、悲伤在270度附近（蓝色系）。饱和度和值与情感特性一致，如高唤醒情感饱和度高。回归模型成功预测颜色属性，多任务学习提高了分类和回归任务的性能。

## 一句话评价
该研究创新地将颜色属性引入语音情感识别，提供了更丰富、可解释的情感表示，并通过多任务学习验证了其有效性。

---

## 5. How Much Does Machine Identity Matter in Anomalous Sound Detection at Test Time?

**作者**: Kevin Wilkinghoff, Keisuke Imoto, Zheng-Hua Tan
**链接**: [2602.16253](https://arxiv.org/abs/2602.16253)
**分类**: Anomalous Sound Detection | **关键词**: anomalous sound detection, machine condition monitoring, evaluation protocols, robustness analysis

## 核心痛点
当前异常声音检测（ASD）评估协议隐含假设测试时机器身份已知，并在机器级别进行评估。然而，在实际监控场景中，多个已知机器并发运行，测试记录可能无法可靠归属到特定机器，这导致部署约束（如每台机器专用传感器）和评估偏差，隐藏了方法鲁棒性差异。

## 方法创新
论文提出一个最小修改的评估协议：在测试时移除机器身份信息，将多个机器的测试记录合并并联合评估，同时保持训练数据和评估指标（如AUC、pAUC）不变。机器身份标签仅用于事后评估，以分析性能退化。此外，引入隐式机器识别任务作为辅助指标，量化异常检测性能下降与识别准确性之间的关系。

## 实验结果
实验使用DCASE挑战数据集（如DCASE2020-2025）和代表性ASD方法（包括判别训练模型、基于预训练嵌入的方法如OpenL3和BEATs、以及机器特定模型）。结果显示，当机器身份不可用时，异常检测性能普遍下降，且下降程度与隐式机器识别准确性强相关。归一化性能退化度量表明，方法鲁棒性差异在标准评估中被隐藏。

## 一句话评价
该研究揭示了ASD标准评估协议的局限性，强调了机器身份假设在实际部署中的不现实性，为开发更稳健和可扩展的监控系统提供了重要见解。

---

## 6. Resp-Agent: An Agent-Based System for Multimodal Respiratory Sound Generation and Disease Diagnosis

**作者**: Pengfei Zhang, Tianxin Xie, Minghao Yang, Li Liu
**链接**: [2602.15909](https://arxiv.org/abs/2602.15909)
**分类**: Multimodal Audio Processing | **关键词**: Respiratory Sound Generation, Disease Diagnosis, Multimodal, Agent-Based System, Flow Matching, Modality Weaving, Resp-229k

### 核心痛点
- **信息丢失**: 将呼吸声音信号转换为频谱图时，丢弃了瞬时声学事件（如爆裂声）和临床上下文，导致性能瓶颈。
- **数据有限**: 现有呼吸声音数据集规模小、类不平衡严重，限制了深度学习的泛化能力。
- **分析与生成脱节**: 当前研究侧重于诊断任务，缺乏统一的生成和诊断框架。

### 方法创新
- **Resp-Agent 系统**: 基于代理的闭环框架，由 Thinker-A2CA 控制器协调，主动识别诊断弱点并调度生成任务。
- **Modality-Weaving Diagnoser**: 通过 Strategic Global Attention 和稀疏音频锚点，早期融合 EHR 文本和音频令牌，捕获长程临床上下文和毫秒级瞬态事件。
- **Flow Matching Generator**: 使用文本条件大型语言模型（LLM）和 BEATs 风格令牌，合成高保真呼吸声音，解耦病理内容和声学风格。
- **Resp-229k 数据集**: 包含 229k 录音配对 LLM 生成的临床叙事，支持多模态建模和跨域评估。

### 实验结果
- Resp-Agent 在多种评估设置中一致优于先前方法，提高了在数据稀缺和长尾类不平衡下的诊断鲁棒性。实验基于 Resp-229k 的跨域分割，验证了泛化能力。

### 一句话评价
Resp-Agent 是一个创新的多模态系统，通过闭环设计统一了呼吸声音的生成和诊断，解决了关键挑战并推动了该领域的进展。

---

## 7. Scaling Open Discrete Audio Foundation Models with Interleaved Semantic, Acoustic, and Text Tokens

**作者**: Potsawee Manakul, Woody Haosheng Gan, Martijn Bartelds, Guangzhi Sun, William Held, Diyi Yang
**链接**: [2602.16687](https://arxiv.org/abs/2602.16687)
**分类**: Audio Foundation Models | **关键词**: Scaling Laws, Discrete Audio Tokens, Interleaved Tokens, SODA, Multimodal Audio

## 核心痛点
当前音频语言模型存在显著限制：文本优先模型（如SALMONN）扩展预训练文本LLM，导致语义瓶颈，无法进行通用音频到音频建模；语义唯一模型（如TWIST）丢弃声学细节，限制高保真理解和生成；原生音频模型（如Moshi）聚焦特定任务，缺乏文本集成。这些方法均未联合建模语义、声学和文本，阻碍了多模态音频AI的发展。

## 方法创新
本文提出原生音频基础模型，采用下一个令牌预测框架，联合建模语义内容、声学细节和文本令牌。关键创新包括：1) 系统研究设计选择（数据源、文本混合比例、令牌组合），建立验证过的训练食谱；2) 首次通过IsoFLOP分析（64个模型，3×10^18到3×10^20 FLOPs）推导离散音频模型的缩放定律；3) 使用话语级交错令牌（避免对齐错误），支持音频延续、文本延续、音频到文本和文本到音频四种能力。

## 实验结果
缩放定律分析显示，最优数据增长快于最优模型大小（D* ∝ C^0.579，N* ∝ C^0.367），即数据增长1.6倍于模型大小。基于此，训练了SODA模型套件（135M到4B参数，500B令牌），验证了缩放预测。SODA作为灵活骨干，在音频和跨模态基准测试中表现竞争性，并通过微调实现语音保留的语音到语音翻译，展示了统一架构的实用性。冷启动训练优于热启动，提供更高稳定性。

## 一句话评价
这篇论文通过系统实证研究，建立了音频基础模型的训练食谱和缩放定律，为多模态音频AI的发展提供了重要基准和开源资源。

---

## 8. Hardware-accelerated graph neural networks: an alternative approach for neuromorphic event-based audio classification and keyword spotting on SoC FPGA

**作者**: Kamil Jeziorek, Piotr Wzorek, Krzysztof Blachut, Hiroshi Nakano, Manon Dampfhoffer, Thomas Mesquida, Hiroaki Nishi, Thomas Dalgaty, Tomasz Kryjak
**链接**: [2602.16442](https://arxiv.org/abs/2602.16442)
**分类**: Speech Recognition | **关键词**: event-based audio processing, graph convolutional neural networks, FPGA, keyword spotting

### 核心痛点
- 随着边缘传感器数据量增加，特别是神经形态设备产生的离散事件流，传统硬件（如GPU）功耗高、微处理器延迟大，且事件数据稀疏性未被充分利用，导致本地处理效率低下。
- 现有事件音频处理方法如脉冲神经网络（SNNs）在硬件实现中存在权重访问模式非确定性问题，难以真正利用数据稀疏性。

### 方法创新
- 提出一种基于SoC FPGA的硬件加速事件图神经网络，用于事件音频分类和关键词识别。
- 使用人工耳蜗（Artificial Cochlea）将时间序列音频信号转换为稀疏事件数据，形成谱时事件图。
- 结合图卷积网络（GCN）和循环神经网络（RNN）进行端到端处理，实现全异步事件逐事件处理，保持数据时空稀疏性。
- 采用硬件感知设计方法进行优化，包括图生成模块修改、图卷积中引入额外归一化，以及超参数选择。

### 实验结果
- **分类任务**：在SHD数据集上，基线浮点模型达到92.7%的准确率，仅低于state-of-the-art 2.4%，但参数减少超过10倍和67倍；在SSC数据集上，模型达到66.9–71.0%的准确率，首次提供硬件加速评估。
- **比较基准**：相比基于FPGA的脉冲神经网络，量化模型达到92.3%的准确率，超越它们达19.3%，同时减少资源使用和延迟。
- **关键词识别任务**：系统达到95%的词尾检测准确率，延迟仅10.53微秒，功耗1.18瓦，为高效能事件驱动关键词识别树立了强基准。

### 一句话评价
这项研究通过FPGA上的事件图神经网络实现，为事件音频处理提供了一个高效、低功耗、低延迟的硬件友好解决方案，在分类和关键词识别任务中达到先进性能。

---

## 9. Real time fault detection in 3D printers using Convolutional Neural Networks and acoustic signals

**作者**: Muhammad Fasih Waheed, Shonda Bernadin
**链接**: [2602.16118](https://arxiv.org/abs/2602.16118)
**分类**: Acoustic-Based Fault Detection in Additive Manufacturing | **关键词**: 3D printing, fault detection, convolutional neural networks, audio signal analysis, real-time monitoring

### 核心痛点
传统3D打印故障检测方法，如视觉检查和硬件传感器，存在成本高、侵入性强、实时监控能力有限、易受环境干扰等问题，难以实现高效、非接触式的监测。

### 方法创新
本论文提出了一种基于声学信号分析和卷积神经网络（CNN）的实时故障检测方法。通过使用音频传感器捕获3D打印机操作时的声音，转换为频谱图（如Mel-spectrograms），并利用CNN模型进行分类，以识别常见机械故障，如喷嘴堵塞、丝料断裂和皮带打滑。该方法采用非接触式监测，结合带通滤波（100–1200 Hz）和噪声减少技术，实现高效、成本效益的实时故障检测。

### 实验结果
初步实验结果表明，音频信号结合机器学习技术能可靠地增强实时故障检测，提供可扩展的解决方案。实验使用Makerbot Method X打印机、Sparkfun音频传感器和ABS材料，通过频谱图分析和CNN模型进行故障分类，但具体性能数据因内容截断未提供。

### 一句话评价
该研究为3D打印故障检测提供了一种创新的AI驱动方法，具有非侵入性、成本低和实时性强的优势，有望提升制造业质量控制并减少生产中断。

---

