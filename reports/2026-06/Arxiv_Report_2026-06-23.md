# Arxiv Daily Deep Report - 2026-06-23

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 46
---

## 1. PHAST-Net: Attention-Guided, Physics-Informed Network for Unified Estimation of Ideal Time-Frequency Representations

**作者**: James M. Cozens, Simon J. Godsill
**链接**: [2606.23665](https://arxiv.org/abs/2606.23665)
**分类**: Time-Frequency Analysis | **关键词**: Ideal Time-Frequency Representation, Physics-Informed, Attention-guided, Continuous Log-frequency Adaptive Wavelet Transform (CLAWT), Harmonic suppression, Tempogram, Metrogram, Cohen's class, Spline-PHAST-Net, Deep learning

## 核心痛点
传统时频分析方法（如WVD、PWVD）在处理多分量信号时面临严重的交叉项干扰，且现有深度学习方法缺乏对变换族一致性的显式约束，难以在抑制交叉项的同时保持高分辨率。此外，针对谐波结构的对数频率域统一处理框架缺乏，且存在谐波抑制、节奏表示（Tempogram、Metrogram）精度不足等问题。

## 方法创新
1. **PHAST-Net框架**：提出一种注意力引导、物理信息驱动的网络，直接从连续对数频率自适应小波变换（CLAWT）星座图估计理想时频表示（ITFR），实现交叉项抑制和自动项锐化。
2. **CLAWT星座构建**：通过Cohen类核分析，在紧致T-F平面上选择覆盖局部方向和尺度的CLAWT集合。
3. **物理信息辅助重构损失**：在训练中引入CLAWT重构损失，保证变换一致性和能量守恒，缓解目标稀疏问题。
4. **对数频率域设计**：利用空间特征变换（SFT）在log-frequency网格上处理，支持谐波结构等变性，进而提出谐波PHAST-Net，可控抑制谐波保留基频轨迹。
5. **Spline-PHAST-Net**：通过Frangi脊检测和数据关联提取连续样条轨迹，支持任意分辨率重渲染和信号重建。
6. **无限合成数据训练**：程序生成包含随机样条轨迹、时变幅度、泛音结构、交叉和噪声的数据，增强泛化能力。

## 实验结果
论文在合成数据和真实语音/音乐上展示了改进的准确性，相比已有方法（如RIFT、CNN-based方法）在交叉项抑制、时频浓度和噪声鲁棒性上有显著提升。谐波PHAST-Net能提取干净的基频Tempogram和Metrogram，支持下游节拍追踪等任务。

## 一句话评价
PHAST-Net统一解决了时频分析中的交叉项抑制、谐波处理、可解释性重建等关键问题，是当前最先进的时频表示估计框架。

---

## 2. Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement

**作者**: Mads Østergaard, Alexander Neergaard Zahid, Karl Ulbæk, Andreas Hansen Bagge, Kenny Falkær Olsen, Rasmus Malik Høegh Lindrup
**链接**: [2606.23332](https://arxiv.org/abs/2606.23332)
**分类**: Speech Enhancement | **关键词**: own-voice cancellation, target speaker extraction, low-latency, Mamba, MinGRU, far-field speech enhancement

## 核心痛点
远程语音增强系统中，设备将增强后的音频流回用户时，因声学往返延迟超过10ms引发可感知的自身语音失真（echo-like artifacts），现有方法延迟高、计算开销大。

## 方法创新
1. **定义新任务**：Own-Voice Cancellation (OVC)——从含噪多说话人混合中移除已注册的目标说话人，保留其余语音，作为目标说话人提取（TSE）的互补任务。
2. **轻量级架构**：提出Mamba-MinGRU遮罩网络，使用Mamba块结合MinGRU时间混合，保持全局上下文且仅需2ms算法延迟。辅助网络替换为线性RNN编码器，进一步降低计算。
3. **条件化机制**：通过注册语音提取说话人嵌入，以元素级乘法调制主网络特征。

## 实验结果
- 在SDR和PMOS指标上，Mamba-MinGRU与TD-SpeakerBeam基线性能相当（非因果~13 dB SDR）。
- 计算效率显著提升：主网络从4.97 GMAC/s降至0.33 GMAC/s（非因果），因果设置下性能保持。
- 线性RNN辅助编码器相比ConvTasNet辅助网络，SDR提升，计算从1.67 GMAC/s降至0.26 GMAC/s。

## 一句话评价
首个系统研究远场语音增强中自身语音抵消的工作，以极低延迟和轻量级模型实现了高效、实用的解决方案。

---

## 3. Word Lengthening as a Function of Utterance Position: A Multi-Corpus Study

**作者**: Mateo Cámara, José Luis Blanco, Juan Ignacio Godino-Llorente, Jeung-Yoon Choi, Stefanie Shattuck-Hufnagel
**链接**: [2606.23232](https://arxiv.org/abs/2606.23232)
**分类**: Speech Prosody and Turn-taking | **关键词**: turn-taking, word lengthening, prosody, boundary lengthening, multi-corpus study

## 论文总结

### 核心痛点
人类对话中话轮转换的高效性需要听者在几百毫秒内预测话轮结束点。以往研究关注句法和语用完成线索，但韵律线索（尤其是边界前延长）的作用尚需量化验证。本文系统研究话轮末尾单词是否比句中单词更长，以及该延长是源于韵律修饰还是词汇选择，并定位延长在单词内的分布。

### 方法创新
- 使用四个大规模语料库（Switchboard, Columbia Games, BU Radio News, Glissando），涵盖对话、任务导向、朗读风格及英语、西班牙语，共>500说话人，约39,500话轮。
- 区分话轮末尾（TF）与句中（MS）位置，严格排除反馈词（如“yeah”）。
- 通过匹配同说话人同词（跨话轮和句内）控制词汇构成，进行配对检验。
- 分析音节级时长，定位延长主要发生在最后音节。
- 利用ToBI边界指数验证与韵律边界强度的对应关系。

### 实验结果
- 话轮末尾单词平均时长0.44s，句中0.24s，差异203.1ms，效应量大（d=1.22）。四个语料库方向一致，效应量d=0.78~1.47。
- 匹配词对比：严格配对（同一录音段）中TF比MS长79.9ms（p<0.001, d=0.59），宽松配对长81.1ms（d=0.69），92.8%的单词显示正效应。
- 音节位置分析：延长集中在最后音节（d=0.89），非最后音节几乎无差异（d=0.01）。
- 边界强度与时长分级相关：低边界0.22s，中0.34s，高0.44s。
- 跨语言（英语 vs. 西班牙语）均呈现强效应。

### 一句话评价
本文通过多语料库大规模分析，稳健地证实了话轮末尾单词延长是跨语言、跨风格的普遍韵律现象，且该延长源于韵律修饰而非词汇选择，主要定位于单词最后音节。

---

## 4. Acoustic Landmark Detector based on Conformer and HuBERT

**作者**: Mateo Cámara, José Luis Blanco, Juan Ignacio Godino-Llorente, Jeung-Yoon Choi, Stefanie Shattuck-Hufnagel
**链接**: [2606.23228](https://arxiv.org/abs/2606.23228)
**分类**: Speech Processing / Acoustic Landmark Detection | **关键词**: acoustic landmarks, landmark detection, Conformer, soft labels, HuBERT, temporal localization, self-supervised learning

## 核心痛点
传统声学标志检测依赖信号处理启发式方法，精度不足；深度学习方法在时序定位和类型识别上仍有挑战，尤其是不同标志类型（如元音 vs 爆破音）的检测难度差异大。

## 方法创新
- 提出基于Conformer编码器的检测系统，14种配置对比。
- 创新性地使用**高斯软标签**（Gaussian soft labels），为每类标志设置不同的时间扩展σ（10-20 ms），模拟人工标注的不确定性，显著提升模型对元音等渐变事件的检测。
- 对比多种特征：mel谱、冻结wav2vec2、冻结HuBERT及混合特征，发现**冻结HuBERT最优**（无需微调）。
- 采用容忍度匹配的F1@20ms评估，强调时序精确性。

## 实验结果
- 最佳配置：HuBERT特征 + 高斯软标签 + Conformer，F1@20ms=0.77，F1@30ms=0.84。
- 软标签相比硬标签提升7.0%绝对F1（元音类从0.18提升至0.54）。
- 爆破音/摩擦音检测可靠（F1>0.80），元音仍具挑战（F1≈0.55）。
- 在自有语料上达到13.8% Landmark Error Rate（LER），与AutoLandmark（31.3%）不可直接比较。

## 一句话评价
该工作系统性地验证了Conformer与自监督特征在声学标志检测中的潜力，高斯软标签策略有效缓解了标注时序歧义，为精细化语音事件检测提供了新思路。

---

## 5. An Acoustic Landmark Database of the English Lexicon via Articulatory Synthesis

**作者**: Mateo Cámara, José Luis Blanco, Juan Ignacio Godino-Llorente, Jeung-Yoon Choi, Stefanie Shattuck-Hufnagel
**链接**: [2606.23220](https://arxiv.org/abs/2606.23220)
**分类**: Speech Synthesis / Acoustic Phonetics | **关键词**: Acoustic landmarks, speech synthesis, articulatory synthesis, acoustic phonetics, Pink Trombone, computational phonetics

## 总结

**核心痛点**：声学地标理论的研究受限于缺乏大规模、准确标注的地标数据集。手动标注成本高、一致性差，且连续语音中的协同发音和弱化现象使得从自然语音中获取可靠标注变得困难。

**方法创新**：提出逆向方法——通过物理合成器生成语音并同时算法生成地标标签。使用 Pink Trombone 声道合成器，直接控制发音参数，在发音事件发生的精确时间点自动放置地标标签（如闭合、释放）。生成了包含超过 20 万个合成词的语料库，覆盖男性和女性两种配置，并附有时间对齐的标注。使用 STOI 度量可懂度。

**实验结果**：报告了地标频率和主导线索模式的统计结果，支持定量研究和自动地标检测器的训练/基准测试。

**一句话评价**：该工作构建了首个大规模、无歧义标注的声学地标数据库，为地标理论验证和自动检测系统提供了可靠基准。

---

## 6. FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech

**作者**: Haoxu Wang, Biao Tian, Weiqing Li, Xiang Lv, Han Zhao, Xiangang Li
**链接**: [2606.23190](https://arxiv.org/abs/2606.23190)
**分类**: Text-to-Speech | **关键词**: text-to-speech, reinforcement learning, flow-matching, group relative policy optimization, speaker similarity, zero-shot voice cloning

## 核心痛点
现有Text-to-Speech (TTS)的强化学习（RL）研究主要集中在大型语言模型（LLM）上，而基于流匹配（Flow-Matching, FM）的TTS模型尚未充分探索。已有的RL方法（如PPO、DPO）需要训练多个辅助模型或大量人工偏好数据，成本高且不稳定。

## 方法创新
1. **首次将Flow-GRPO引入TTS**：通过将常微分方程（ODE）轨迹转换为随机微分方程（SDE）路径，为FM模型引入随机性，无需额外训练随机生成器，即可直接微调开源FM模型。
2. **简化RL流程**：无需价值网络、偏好对或令牌到奖励模型，直接利用现成的奖励信号。
3. **多目标奖励优化**：分析奖励冲突，提出加权组合（带标准差归一化）比概率组合收敛更快更稳定。
4. **三种实用优化**：①训练时省略无分类器引导（CFG）加速收敛；②合成难例提升鲁棒性；③对FM组件应用RL主要改善音频细节指标，而对LM应用RL改善可懂度（针对LLM-FM混合模型）。

## 实验结果
- **模型**：在CosyVoice 3.0（LLM-FM混合）和F5-TTS（纯FM）上评估。
- **指标**：说话人相似度、感知质量（DNSMOS）显著提升；F5-TTS还降低了词错误率（WER）。
- **泛化能力**：在不同说话人验证模型、语言和LLM前端下表现鲁棒。

## 一句话评价
首个将在线强化学习成功应用于流匹配TTS的工作，通过SDE转换实现无需辅助模型的直接微调，并验证了多目标奖励加权组合的有效性。

---

## 7. Audio Editing in the Era of Foundation Models: A Survey

**作者**: Changhao Pan, Yifei Fan, Fan Zhuo, Yifu Chen, Wenxiang Guo, Yu Zhang, Ruiqi Li, Zhiyuan Zhu, Rui Yang, Shengpeng Ji, Chenyuhao Wen, Jiayang Xu, Ke Lei, Xiaoda Yang, Jingyu Lu, Zhou Zhao
**链接**: [2606.23139](https://arxiv.org/abs/2606.23139)
**分类**: Audio Editing, AIGC | **关键词**: 音频编辑, 基础模型, 扩散模型, 编解码语言模型, 声学编辑, 语义编辑, 实例编辑, AIGC, 综述

## 核心痛点
当前音频编辑领域缺乏系统性的综述，现有综述多聚焦于音频语言模型、口语语言模型或通用音频生成，对基于基础模型的音频编辑讨论不足。音频编辑任务多样，从精细的局部修改到全局变换，且对可控性、时间定位和内容保持有不同要求。

## 方法创新
本文提出统一的任务分类法，将音频编辑分为三大类：声学编辑（响度、降噪、混响、均衡）、语义编辑（语言、表达、风格）和实例编辑（替换、删除/提取、插入、叠加）。总结了基于基础模型的两种主要范式：
1. **基于Token的编解码语言模型**：将音频转换为离散token序列，通过自回归填充或选择性重生成进行编辑。代表工作包括AudioLM、VALL-E、VoiceCraft、SpeechX等。
2. **扩散与流匹配模型**：在连续声学空间（如梅尔谱）中进行条件去噪或流变换，适用于高保真重建和细粒度控制。代表工作包括WaveGrad、F5TTS、AudioLDM、Stable Audio等。

此外，从训练策略上分为基于训练和免训练方法，并整理了相关资源（数据集、评估协议、数据构建工具）。

## 一句话评价
本文是首个系统综述基础模型时代音频编辑的论文，提出了统一的任务分类法并总结了主流范式，为后续研究提供了清晰的框架和资源汇总。

---

## 8. AudioCALM: Continuous Autoregressive Language Modeling for Universal Audio Generation

**作者**: Huadai Liu, Kaicheng Luo, Wen Wang, Qian Chen, Bin Ma, Xiangang Li, Wei Xue
**链接**: [2606.23080](https://arxiv.org/abs/2606.23080)
**分类**: Audio Generation | **关键词**: Continuous Autoregressive Language Modeling, Flow Matching, Asymmetric Mixture-of-Modality-Experts, Universal Audio Generation, Text-to-Speech, Text-to-Sound, Text-to-Music

# AudioCALM: Continuous Autoregressive Language Modeling for Universal Audio Generation

## 核心痛点
现有音频生成范式（离散token自回归、级联LM+生成器、非自回归流匹配）均存在局限性：离散token方法受限于信息瓶颈（尤其对多音音乐和环境声音），级联方法牺牲端到端优化，非自回归方法缺乏上下文理解和自然变长生成。此外，统一语音、声音和音乐生成时存在text–audio不对称性：语音需要局部对齐注意力，而声音和音乐需要全局扩散注意力，混合训练会降低非语音生成质量。

## 方法创新
1. **Continuous Autoregressive Language Modeling (CALM)**: 将自回归下一个token预测从离散token扩展到连续音频隐空间，用流匹配头替代softmax，在每一位置预测rectified-flow速度，保留LM接口的同时避免离散化瓶颈。
2. **AR-Flow注意力模式**: 块因果注意，每个隐块通过流匹配生成，同时自回归地关注所有先前块和完整文本条件，支持任意长度生成。
3. **Data reformulation**: 使用多模态LLM将语音转录、声音/音乐短描述统一为长格式描述，统一条件化接口，并支持零样本语音克隆。
4. **Asymmetric Mixture-of-Modality-Experts (A-MoME)**: 不对称设计，自注意力和共享FFN对所有模态共用，仅对语音添加专用残差专家，声音和音乐共享主干，不增加非语音推理开销。

## 实验结果
AudioCALM在语音、声音和音乐生成基准上均达到或超越域特定SOTA，并优于先前统一模型。

## 一句话评价
AudioCALM通过连续隐空间自回归流匹配和不对称模态专家设计，首次在同一模型中实现了高质量、端到端、可变长度的统一语音、声音和音乐生成。

---

## 9. STAR-VAE: Structured Topology-Aware Regularization for Audio Reconstruction and Generation

**作者**: Huadai Liu, Wen Wang, Kaicheng Luo, Qian Chen, Xiangang Li, Wei Xue
**链接**: [2606.23064](https://arxiv.org/abs/2606.23064)
**分类**: Audio Generation / Audio Reconstruction | **关键词**: STAR-VAE, Structured Topology-Aware Regularization, Rate-Distortion-Regularity Trilemma, Audio Reconstruction, Audio Generation, Variational Autoencoder, Flow Matching, Mamba

## 核心痛点
论文揭示了音频VAE中存在的**Rate-Distortion-Regularity Trilemma**（率-失真-正则化三难问题）：标准各向同性高斯先验假设所有潜在通道具有同等容量，与音频信号的频谱层次（低频结构可压缩，高频纹理随机不可压缩）不匹配，导致**无序信息打包**（Disordered Information Packing），即关键语义与高频噪声随机交织，损害重建保真度和潜在空间规整性。

## 方法创新
1. **Structured Topology-Aware Regularization (STAR)**：通用训练策略，通过按通道施加梯度约束（容量梯度）重塑潜在空间几何，将结构信息路由到高容量通道（低KL惩罚），纹理信息路由到低容量通道（高KL惩罚），从而解决三难问题。
2. **STAR-VAE**：结合STAR与混合CNN-Mamba架构，利用CNN局部特征提取和Mamba线性复杂度全局建模，避免高容量编码器在均匀KL下出现的“重建漂移”。
3. **STAR-Gen**：基于LLM的Flow Matching生成框架，利用STAR-VAE结构化的潜在空间实现高保真文本到音频生成，无矢量量化伪影。

## 实验结果
STAR-VAE在多种音频域（声音、音乐）上达到最先进的重建保真度，显著优于基线（如标准VAEs、CNN-based VAEs）；结构化潜在空间同时改进了传统扩散模型和STAR-Gen的生成性能，在文本到音频生成任务中取得SOTA。消融实验证实STAR诱导层次化信息组织、防止重建漂移。

## 一句话评价
本文通过拓扑感知正则化巧妙化解音频VAE的容量-保真度-规整性矛盾，为高质量音频生成提供了简洁有效的通用解决方案。

---

## 10. CAAD: Contrastive Audio-Aware Distillation for Efficient Speech Language Models

**作者**: Chun-Wei Chen, Tzu-Quan Lin, Ke-Han Lu, Wei-Ping Huang, Hung-Yi Lee
**链接**: [2606.23052](https://arxiv.org/abs/2606.23052)
**分类**: Speech Language Model Knowledge Distillation | **关键词**: Contrastive Audio-Aware Distillation, Knowledge Distillation, Speech Language Model, Modality Bias, Contrastive Decoding

## 核心痛点
大型语音语言模型（SLMs）参数庞大、推理延迟高，且存在模态偏差，即模型过度依赖语言先验而忽视声学特征。对比解码（CD）虽能缓解此问题，但需双路径逐token生成，推理延迟翻倍，训练开销巨大。

## 方法创新
提出**对比音频感知蒸馏（CAAD）**，两阶段框架：
1. **阶段1：Pseudo-GT生成**——利用DeSTA框架从音频元数据（如性别、情感、声学环境）生成伪真值序列作为统一锚点。
2. **阶段2：对比音频感知蒸馏**——同步教师强制策略同时计算正路径（音频+文本）和负路径（仅文本）的logits，通过外推得到音频感知目标，让学生模型通过KL散度和交叉熵损失学习。

关键创新：同步教师强制策略实现全序列并行化，避免逐token生成的计算开销。

## 实验结果
- 在Dynamic-SUPERB上相比标准知识蒸馏获得约8%的相对提升。
- 在MCR-BENCH上有效缓解语言偏差，学生模型在副语言任务上超越教师模型贪婪解码性能。
- 训练仅优化32M参数（Q-Former适配器），总训练时间70小时（RTX A6000）。

## 一句话评价
CAAD通过同步教师强制策略将对比解码的推理开销转移到训练中，高效蒸馏出音频感知能力，实现低延迟且抗偏差的语音语言模型。

---

## 11. Domain-incremental audio classification using domain-specific experts and prototype classifier

**作者**: Jongyeon Park, Do-Hyeon Lim, Sang-won Park, Hong Kook Kim, Kyungdeuk Ko, Hyeongcheol Geum, Jeong Eun Lim
**链接**: [2606.22952](https://arxiv.org/abs/2606.22952)
**分类**: Domain-incremental audio classification | **关键词**: Domain-incremental learning, continual learning, sound event classification, prototype classifier, feature imputation, generative replay, DeepInversion, catastrophic forgetting

本文针对DCASE 2026 Challenge Task 7的域增量音频分类问题，提出了一种基于域特定专家和原型分类器的系统。核心痛点在于模型在增量阶段无法同时访问过去和未来的域数据，易发生灾难性遗忘。方法创新包括：1) 使用多个冻结的域特定专家，每个专家在各自域训练后固定，避免参数干扰；2) 采用DeepInversion生成合成数据回放，保留过去域知识；3) 基于原型学习的余弦原型分类器，将各专家高层特征拼接后归一化，通过可学习温度缩放进行软分类；4) 针对特征缺失问题，训练跨阶段回归插补器，利用完整数据预测缺失特征。实验结果表明，提交的四个系统在开发集上达到78.38%微平均和78.92%宏平均准确率，远超官方基线。一句话评价：该方法通过冻结专家和原型分类器有效缓解灾难性遗忘，在域增量学习任务上取得显著提升。

---

## 12. Explainable AI in Speaker Recognition -- Attention Map Visualisation and Evaluation

**作者**: Yanze Xu, Mark D. Plumbley, Wenwu Wang
**链接**: [2606.22901](https://arxiv.org/abs/2606.22901)
**分类**: Explainable AI | **关键词**: Explainable AI, Speaker Recognition, Attention Map Visualization, Attention Map Evaluation, Class Activation Map, GradCAM, LayerCAM, RISE-eval

## 核心痛点
现有注意力图评估方法（如RISE-eval）存在两个问题：1) 某些条件下不同注意力图的评估结果难以区分；2) 评估过程受与注意力图质量无关的因素干扰。

## 方法创新
提出Modified RISE-eval算法，针对上述缺点进行改进，通过优化输入采样和评估机制，使评估结果更可靠。

## 实验结果
在说话人识别任务中，使用GradCAM和LayerCAM生成注意力图，并用Modified RISE-eval进行评估。结果表明：GradCAM在利用最深网络层激活图时更好，LayerCAM在利用较浅层激活图时更好。

## 一句话评价
本文系统梳理注意力图评估方法，提出改进算法，为XAI在说话人识别中的应用提供了有效工具。

---

## 13. MSU-Bench: Towards Speaker-Centric Understanding in Conversational Multi-Speaker Scenarios

**作者**: Zhaokai Sun, Shuai Wang, Zhennan Lin, Chengyou Wang, Dehui Gao, Yuang Cao, Chunjiang He, Pan Zhou, Lei Xie
**链接**: [2606.22868](https://arxiv.org/abs/2606.22868)
**分类**: Spoken Language Understanding Benchmarking | **关键词**: MSU-Bench, multi-speaker conversational understanding, speaker-centric evaluation, large audio language models, benchmark, speaker grounding, dialogue reasoning

## 核心痛点
现有的语音理解基准主要聚焦于单说话人场景或孤立子任务，缺乏对真实多说话人对话中说话者中心理解能力的系统性评估。

## 方法创新
- 提出MSU-Bench基准，包含16个说话者中心任务和2300个QA实例，采用两层任务层次：从说话者定位（Tier1）到多说话者对话推理（Tier2）。
- 构建了可扩展的流水线：使用Gemini进行对话质量评估、说话者感知标注和QA生成，并引入人工验证确保答案确定性和标签正确性。
- 定义了五种说话者引用方案（无索引、时间索引、文本索引、说话者索引、复合索引）以控制定位难度，并通过错误选项设计支持诊断性错误分析。

## 实验结果
- 评估了9个语音语言模型（6个开源、3个闭源），闭源系统（Gemini-3-Flash总体0.77）显著领先开源模型（最佳MiMoAudio为0.56）。
- 开源模型在说话者属性识别、观点聚合和对话推理任务上表现较弱；闭源模型在复杂定位和推理上仍有提升空间。
- 诊断分析表明，错误主要源于错误说话者分配、幻觉和格式违规。

## 一句话评价
MSU-Bench填补了多说话者对话理解基准的空白，揭示了现有模型在说话者定位与推理上的关键瓶颈。

---

## 14. Bridging Self-Supervised Learning and Speech Enhancement: A Wav2Vec2-Conditioned Framework

**作者**: Shuubham Ojha, Carol Espy-Wilson
**链接**: [2606.22591](https://arxiv.org/abs/2606.22591)
**分类**: Speech Enhancement | **关键词**: diffusion models, self-supervised learning, wav2vec 2.0, feature-wise linear modulation, speech enhancement

### 核心痛点
现有扩散模型用于语音增强时缺乏语言指导，导致泛化能力不足，尤其在未知噪声环境下性能下降。

### 方法创新
提出一种基于wav2vec 2.0特征的条件扩散模型：使用预训练的wav2vec 2.0从带噪语音中提取语音特征，通过特征线性调制（FiLM）注入U-Net瓶颈层。为压缩时间序列，推导出基于线性高斯状态空间模型的指数平滑（EMA）作为最优因果聚集策略，以单个缩放-平移对调节瓶颈。FiLM生成网络仅有少量可训练参数，保持轻量。

### 实验结果
在VoiceBank-DEMAND和LibriMix数据集上评估，与StoRM基线相比：
- PESQ提升约0.4（例如OURS-128达到2.8742 vs StoRM-128的2.4862）
- STOI和DNSMOS（SIG, BAK, OVRL）均有提升
- SI-SDR略有下降（例如17.9844 vs 18.5656），但整体性价比高
- 消融实验显示平滑系数α=1.0最优，且瓶颈处FiLM效果最好
- 推理速度方面，32通道模型可实时处理（RTF=0.55）

### 一句话评价
该工作通过将自监督特征作为条件信号有效引导扩散语音增强，在感知质量上显著超越现有方法，且计算开销小。

---

## 15. A DDSP Framework for Adaptive Room Equalization

**作者**: F. Marcos-Macias, M. P. Daza-Llin, M. Camara, J. L. Blanco
**链接**: [2606.22563](https://arxiv.org/abs/2606.22563)
**分类**: Audio Enhancement | **关键词**: DDSP, adaptive room equalization, Fx-LMS, differentiable signal processing, parametric equalizer, closed-loop control

## 核心痛点
传统自适应房间均衡方法（如Fx-LMS）在处理时变声学条件和复杂激励信号（如音乐）时表现不佳，因其刚性公式难以适应动态变化。

## 方法创新
提出一种基于可微数字信号处理（DDSP）的模块化框架，用于闭环自适应房间均衡。该框架支持可互换的均衡器结构、响应估计方法、损失函数和优化器，并通过自动微分将经典Fx-LMS作为特例包含在内。实验采用时变测量的房间冲激响应，对比了时域和频域损失函数，并分析了在线房间响应估计精度和帧长度对性能的影响。

## 实验结果
相对于非均衡响应，系统距离降低70%，在最差情况下mel谱距离降低13%。频域目标函数比时域更稳定。框架提供了开源PyTorch实现。

## 一句话评价
该工作通过模块化DDSP框架统一了传统自适应滤波与可微信号处理，为探索自适应房间均衡新方法提供了基础。

---

## 16. Learning from Audio-Dependency Errors: Data Curation Strategies Based on Model Confusion Patterns in Audio Question Answering

**作者**: Hyeonuk Nam
**链接**: [2606.22276](https://arxiv.org/abs/2606.22276)
**分类**: Audio Question Answering | **关键词**: Audio Question Answering, Data Curation, Model Confusion Patterns, Audio-Dependency, Qwen3-Omni, LoRA Fine-Tuning, DCASE Challenge

## 核心痛点
音频问答任务中，许多问题仅凭文本先验即可正确回答，导致模型不依赖音频证据，而任务要求模型必须基于音频内容作答。初步实验发现，即使移除音频，强开放音频语言模型仍能回答大部分样本，这削弱了音频推理的必要性。

## 方法创新
提出基于模型困惑模式的数据筛选策略（Audio-Dependency-Aware Data Curation）。在微调前，对Qwen3-Omni模型进行三种输入条件的诊断推理：正常音频-问题对、空音频、打乱音频。根据模型在不同条件下的正确性（N, E, S）将训练样本分为多个桶（如强音频依赖、文本先验、打乱泄露等）。微调时仅使用**强音频依赖样本**（N=1, E=0, S=0），并添加少量空音频负样本（目标为“无法从音频确定”），同时使用文本-only响应归一化器处理解析失败的生成。此外，通过冻结音频塔和多模态投影器、使用LoRA低秩适配进行高效微调。

## 实验结果
- 最佳单模型（训练集-only）在官方开发集上达到**67.27%**准确率（含响应归一化），优于本地Qwen3-Omni基线（65.90%）。
- 关键发现：仅使用强音频依赖子集（约占训练集24.3%）并搭配5%空音频负样本时效果最佳；扩大训练集（如加入困难样本或弱音频依赖样本）反而导致性能下降。
- 其他试验（如DPO、GRPO、类别路由、CoT微调）均未超越所提简单SFT方案。

## 一句话评价
通过数据筛选聚焦音频依赖样本，有效提升模型音频问答性能，是一种简洁且高效的数据质量优化范式。

---

## 17. DSSCNet: A Transfer Learning Framework for Cross-Corpus Dysarthric Speech Severity Classification

**作者**: Arnab Kumar Roy, Hemant Kumar Kathania, Paban Sapkota, Sudarsana Reddy Kadiri, Shrikanth Narayanan
**链接**: [2606.22178](https://arxiv.org/abs/2606.22178)
**分类**: Speech Severity Classification | **关键词**: dysarthria, severity classification, transfer learning, fine-tuning, convolutional neural network, squeeze-excitation, residual network

### 核心痛点
构音障碍语音严重程度分类面临说话人变异性、类别不平衡和数据集有限等挑战，现有模型在不同语料库间的通用性差。

### 方法创新
提出DSSCNet框架，结合卷积神经网络（CNN）、Squeeze-and-Excitation网络（SENet）和残差网络（ResNet），通过跨语料库预训练和微调策略提升说话人无关（SI）分类性能。在TORGO和UA-Speech数据集上进行跨库迁移实验（UA-Speech→TORGO和TORGO→UA-Speech）。

### 实验结果
- 说话人依赖实验：TORGO准确率97.66%，UA-Speech准确率98.94%。
- 说话人无关跨库微调：TORGO上准确率75.80%（提升明显），UA-Speech上准确率68.25%。
- 相比基线模型，误分类错误显著减少。

### 一句话评价
DSSCNet通过知识迁移有效提升跨语料库构音障碍严重程度分类的鲁棒性和泛化能力。

---

## 18. How Well Do Self-Supervised Speech Models Encode Age and Gender in Children's Speech? A Layer-Wise Analysis Across Multiple Architectures

**作者**: Abhijit Sinha, Hemant Kumar Kathania, Mohit Joshi, Harishankar Kumar, Shrikanth Narayanan, Sudarsana Reddy Kadiri
**链接**: [2606.22177](https://arxiv.org/abs/2606.22177)
**分类**: 儿童语音分析 / 自监督学习 | **关键词**: 儿童语音, 自监督学习, 年龄分类, 性别分类, Wav2Vec2, HuBERT, Data2Vec, WavLM, 逐层分析, PCA降维

## 核心痛点
儿童语音因生理和认知发展导致的音高波动、共振峰变化、发音模式差异等，使得年龄和性别分类极具挑战。现有方法多针对成人语音，且缺乏对自监督模型各层编码能力的系统分析。

## 方法创新
- 对四种主流SSL模型（Wav2Vec2、HuBERT、Data2Vec、WavLM）进行逐层特征提取，并用轻量CNN分类器评估各层对年龄和性别的编码能力。
- 应用PCA降维优化特征，分析紧凑性和冗余度。
- 在PFSTAR和CMU Kids两个基准儿童语音数据集上，进行了说话人交叉验证、层聚合、跨数据库评估和短时语音段（1-3秒）的鲁棒性测试。

## 实验结果
- 年龄和性别信息在各层分布不均，早期至中层（low-to-mid layers）包含最强的副语言线索。
- HuBERT在年龄分类上表现最佳；Wav2Vec2和HuBERT分别在PFSTAR和CMU Kids上性别分类领先。
- 降维提升性能，短语音段也能实现可靠分类。

## 一句话评价
该研究系统揭示了SSL模型在儿童语音年龄与性别分类中层间信息分布规律，证明了无需微调即可利用早期层特征取得良好效果，为低资源儿童语音应用提供了实用指导。

---

## 19. Using Phonological-Level Wav2Vec2 for Mandarin Automatic Mispronunciation Detection and Diagnosis

**作者**: Jinghao Chen, Mostafa Shahin, Beena Ahmed
**链接**: [2606.22022](https://arxiv.org/abs/2606.22022)
**分类**: Mispronunciation Detection and Diagnosis | **关键词**: Mispronunciation Detection and Diagnosis, Phonological Features, Wav2Vec2, Mandarin, CTC

## 核心痛点
现有 Mandarin MDD 方法主要关注音素级检测精度，但未能显式分离音段与声调错误，导致诊断反馈有限，缺乏对发音错误成因的细粒度解释。

## 方法创新
提出基于音韵特征的 MDD 框架，在统一的 Wav2Vec2-CTC 架构中联合建模音段属性（如发音方式、部位）和声调属性（分类标签或音高目标描述符）。通过将音素分解为低层音韵成分，实现更详细、可解释的诊断反馈。

## 实验结果
相比仅用音素的基线系统，所提方法在 LATIC 非母语语料库上将误接受率（FAR）降低 10.1%，诊断错误率（DER）降低 23.6%。跨语料库泛化测试（AISHELL-1）中，属性识别错误率（AER）降低超 40%（IPA-D vs IPA-S）。

## 一句话评价
首个系统性联合建模音段与声调属性的 Mandarin MDD 框架，有效提升了诊断细粒度和准确性。

---

## 20. ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion

**作者**: Jeongsoo Choi, Ji-Hoon Kim, Shujie Hu, Joon Son Chung
**链接**: [2606.21888](https://arxiv.org/abs/2606.21888)
**分类**: Voice Conversion | **关键词**: neural speech codec, voice conversion, prosody modeling, conditional residual, diffusion autoencoder

## 论文总结

### 核心痛点
传统神经语音编解码器（如EnCodec、SoundStream）学习整体表示，将语言内容、说话人身份和韵律交织在一起。虽然对零样本语音克隆有效，但在需要精确控制或保留韵律的任务（如语音转换）中，这种缠结使得难以在不改变内容或音色的情况下操控韵律。

### 方法创新
ProsoCodec提出将韵律建模为条件残差，而非解耦的独立流：
- **显式文本和说话人先验**：利用预训练ASR提取文本转录，利用预训练SV提取说话人嵌入，作为前缀令牌同时注入编码器和解码器。
- **离散瓶颈**：通过二进制球面量化（BSQ）形成严格的信息瓶颈，迫使离散令牌只捕获未被内容和说话人解释的韵律变化（如语调、节奏）。
- **低频mel带约束**：编码器仅输入低频mel谱（0-4kHz），因为韵律线索主要存在于低频区域。
- **双话语训练策略**：训练时使用同一说话人的两段不同话语分别作为源和参考，避免推理时参考话语的韵律泄漏到输出中。
- **扩散解码器**：基于DiT的流匹配模型，以参考mel谱和源令牌为条件重构高质量mel谱。

### 实验结果
- **客观指标**：在LibriTTS和VCTK上，ProsoCodec在内容保留（WER 4.451）、音色相似度（SIM_r 0.565）、韵律保留（RMSE 0.428, P-MOS 3.852）上优于DDDM-VC、UniAudio、HierSpeech++、FACodec、Seed-VC、Vevo等基线。
- **主观指标**：韵律MOS（P-MOS）和自然度MOS（N-MOS）均为最高或次高。
- **消融实验**：验证了低频mel、双话语训练、条件先验等组件的有效性。

### 一句话评价
ProsoCodec通过将韵律视为条件残差，结合显式先验和精心设计的训练策略，在语音转换中实现了出色的韵律保留和音色迁移，无需复杂的对抗解耦。

---

## 21. ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

**作者**: Masao Someki, Alexander Polok, Carlos Carvalho, Chyi-Jiunn Lin, Da-Hee Yang, Jiatong Shi, Jinchuan Tian, Nelson Enrique Yalta Soplin, Samuele Cornell, Siddhant Arora, Francisco Teixeira, Wei Wang, William Chen, Alberto Abad, Chenda Li, Shinji Watanabe, Wangyou Zhang
**链接**: [2606.21854](https://arxiv.org/abs/2606.21854)
**分类**: 语音和音频研究框架（Speech and Audio Research Framework） | **关键词**: ESPnet3, 大规模训练, 数据集分片, DataOrganizer, 模块化系统架构, 配置驱动, 分布式训练, 参数高效微调

# ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

## 核心痛点
现有语音研究框架（如ESPnet2）在处理大规模数据集（百万小时级）和复杂模型时存在工程负担重、实验逻辑与核心组件耦合紧密、数据集集成和迭代效率低等问题。例如，在ESPnet2中为Whisper添加LoRA支持需要修改超过20个文件和670行代码。

## 方法创新
1. **配置驱动的数据抽象（DataOrganizer）**：基于Hydra的YAML配置，将数据集声明式组合，支持模块化集成和分片迭代，显著减少数据集准备和混合的代码量。
2. **数据集分片（Dataset Sharding）**：通过分片级别迭代和排名感知轮换，减少内存开销和数据集刷新时间，支持大规模高效训练。
3. **模块化系统架构**：将实验逻辑与框架核心分离，通过BaseSystem类集中管理通用工作流阶段（如训练、推理），支持轻量级配方特定重写。
4. **端到端工作流**：统一数据集处理、训练、评估、推理和发布流程，集成评估平台VERSA。

## 实验结果
- **预训练实验（OWSM V4，102M参数）**：相比ESPnet2，每epoch训练时间减少21.1分钟（相对22.2%），多节点GPU利用率稳定超过80%。数据集刷新时间从311.5秒降至13.1秒，内存使用从35.9GB降至73.1MB。
- **微调实验**：新模型和数据集集成仅需约46行额外代码。
- **工程简化**：OWSM训练配方的编排代码从2289行减少到70行（ESPnet2→ESPnet3）。

## 一句话评价
ESPnet3通过模块化架构和配置驱动的数据管理，显著降低了大规模语音研究和实验的工程复杂性，提升了可扩展性和开发效率。

---

## 22. Bridging the Age Gap: Towards Detecting Neural Audio Codec Synthesized Elderly Speech Deepfake

**作者**: Orchid Chetia Phukan, Girish, Mohd Mujtaba Akhtar, Chi-Chun Lee
**链接**: [2606.21735](https://arxiv.org/abs/2606.21735)
**分类**: Speech Deepfake Detection | **关键词**: CodecFake Detection, Elderly Speech, Multimodal Foundation Models, Jensen-Shannon Divergence, BONSAI, Audio Deepfake Detection

## 核心痛点
现有 CodecFake（CF）检测器主要针对年轻成人语音，对老年人语音（具有独特声学特征如气息声增加、音高稳定性下降等）泛化能力极差，且缺乏专门的数据集和方法。

## 方法创新
1. 提出 **Elderly CodecFake Detection (ECFD)** 任务，并发布 **Elderly-CodecFake (ECF)** 数据集（英/中文，含14种NAC变体）。
2. 假设并验证多模态基础模型（FM）如 LanguageBind (LB) 和 ImageBind (IB) 因跨模态预训练（接触老年人视觉场景）更适用于 ECFD。
3. 提出 **BONSAI** 框架，利用 **Jensen-Shannon Divergence (JSD)** 作为融合机制，对齐不同 FM 的表示分布，优于拼接或线性融合。

## 实验结果
- BONSAI 融合 LB 和 IB 在 ECFD 任务上达到 **平均 EER 1.66%**，超越独立 FM 及 SOTA 基线（如 Wav2vec2+AASIST 等）。
- 现有 CF 检测器在老年人语音上性能大幅下降，凸显跨人口统计脆弱性。

## 一句话评价
首个针对老年人语音 CodecFake 检测的基准工作，通过多模态 FM 融合有效解决年龄域偏移问题。

---

## 23. Towards Detecting Neural Audio Codec Synthesized Heart Sounds

**作者**: Girish, Orchid Chetia Phukan, Mohd Mujtaba Akhtar, Bhavinkumar Vinodbhai Kuwar, Swarup Ranjan Behera, Arun Balaji Buduru
**链接**: [2606.21727](https://arxiv.org/abs/2606.21727)
**分类**: Audio Deepfake Detection | **关键词**: Synthetic Heart Sound Detection, Phonocardiograms, Neural Audio Codecs, Spoofing Attack Detection, Self-Supervised Learning, Grammian Optimal Transport, GROOT, CARDIOFAKE

## 核心痛点
心音（Phonocardiogram, PCG）作为一种有前景的生物特征模态，具有独特性和内在活性，传统上难以伪造。然而，随着神经音频编解码器（Neural Audio Codec, NAC）合成技术的快速发展，攻击者可以生成感知上无法区分的伪造心音，对心音生物识别系统构成严重威胁。现有研究缺乏针对这一新型伪造攻击的系统检测方法。

## 方法创新
1. **新任务与数据集**：提出了**合成心音检测（Synthetic Heart Sound Detection, SHAC）**任务，并发布了首个基准数据集**CARDIOFAKE**，包含3163条真实心音和22141条由7种NAC（DAC、Encodec、Soundstream、Speech Tokenizer、FunCodec、AudioDec、SNAC）合成的伪造心音。数据集设置了seen（训练/测试使用相同NAC）和unseen（使用不同NAC以评估泛化能力）两种评估设置。
2. **特征探索**：系统评估了谱特征（MFCC、LFCC）和自监督学习（SSL）表示（Wav2vec2、Unispeech-SAT、WavLM）在SHAC任务上的表现。
3. **融合框架GROOT**：提出**Grammian Optimal Transport**融合机制，通过计算特征格拉姆矩阵的Frobenius距离构建代价矩阵，利用Sinkhorn算法获得最优传输计划，实现谱特征与SSL特征的对齐与融合，充分发挥其互补性（谱特征对声学失真敏感，SSL特征捕捉全局时间结构）。

## 实验结果
实验表明，GROOT将MFCC与WavLM融合后取得了最先进性能，优于单一特征表示及其他竞争基线，验证了谱-SSL融合的有效性。封闭身份识别实验进一步确认了NAC合成心音保留患者身份信息，凸显了检测的紧迫性。

## 一句话评价
本文首次系统研究心音伪造检测，提出基准数据集与创新融合框架，为心音生物识别安全提供了重要基础。

---

## 24. Vaani Benchmark V1.0: An Inclusive Multimodal Benchmark Dataset for Hindi

**作者**: Sujith Pulikodan, Agneedh Basu, Saurabh Kumar, Pranav Bhat, Pavan Kumar J, Visruth Sanka, Nihar Desai, Prasanta Kumar Ghosh
**链接**: [2606.21408](https://arxiv.org/abs/2606.21408)
**分类**: Speech Recognition Benchmark | **关键词**: Hindi ASR, benchmark dataset, multi-reference transcription, multimodal, geographic diversity, code-switching, noise annotation, Vaani project

## 核心痛点
现有印地语自动语音识别（ASR）基准数据集在地理多样性、人口统计代表性及转录鲁棒性方面存在明显不足：大多仅覆盖少量地区，缺乏对方言和口音差异的充分覆盖；每个音频片段仅提供单一参考转录，忽略了同一语音内容可能存在多种有效转录的主观性；对代码切换（code-switching）和噪声场景的标注不足；此外，缺乏多模态（图像+语音）的基准数据，难以评估多模态ASR模型。

## 方法创新
本文提出 **Vaani Benchmark V1.0**，一个面向印地语的包容性多模态基准数据集。
- **数据来源**：从Vaani项目中采集自发语音，通过让说话者描述图像（共8,315张图像）来诱导自然口语。
- **地理覆盖**：覆盖印度22个邦/中央直辖区、104个地区，共3,252位说话者，总时长20.64小时。
- **多参考转录**：每个音频片段由三位独立转录者生成三份参考转录，支持多参考WER计算，更公平地评估ASR系统。
- **丰富元数据**：包括说话者ID、已知语言、居住地邮政编码、邦信息、性别等；明确标注代码切换内容（同时提供本地文字和原文字转录）及非语音事件/噪声。
- **质量控制**：经过多轮人工与自动化检查，确保转录准确性；转录者来自同一地区以保证方言熟悉度。
- **公开/闭集分割**：每个地区50%数据公开，其余作为闭集用于排行榜，防止过拟合。

## 实验结果
基准测试了多个开源和闭源ASR模型，采用三种WER计算方式：Approach 1（单参考）、Approach 2（最优参考选择）、Approach 3（多参考对齐联合计算）。核心结果如下：
- **Vaani Fast Conformer**（开源）表现最佳，Approach 3下WER为10.6%，各方法平均WER 15.2%。
- **Gemini-3.1-Pro**（闭源）紧随其后，Approach 3 WER 11.9%。
- **Sarvam Saaras v3**、**Indic-conformer-600m-multilingual** 等模型也进行了对比。
- 区域性分析显示WER随地区变化显著（标准差约4-5%），验证了地理多样性的重要性。
- 多参考方法（Approach 3）显著降低了WER，说明传统单参考可能高估错误率。

## 一句话评价
Vaani Benchmark通过大规模多参考转录、全面地理覆盖和多模态设计，为印地语ASR系统提供了更包容、更公平且贴近实际的评估基准，填补了现有数据集的关键空白。

---

## 25. Sexualised synthetic personas encode and amplify gendered power asymmetries through voice

**作者**: Alice Ross, Ariadna Sanchez, Elin Kanhov, Catherine Lai, Eva Szekely
**链接**: [2606.21366](https://arxiv.org/abs/2606.21366)
**分类**: Text-to-Speech | **关键词**: text-to-speech, voice AI, gender representation, feminist HCI, speech perception

## 核心痛点
商业语音AI平台（如ElevenLabs）提供的性化合成声音可能强化性别刻板印象和权力不对称，尤其是女性声音常被性化和顺从化，男性声音则被赋予支配和积极特质。

## 方法创新
1. 结合定量形容词选择、定性自由文本响应和声学分析的多模态听力实验。
2. 控制文本内容（性化 vs 中性）和声音性别，分离声学特征和语言内容的影响。
3. 招募多元性别和性取向的参与者（包括非异性恋群体），增强代表性。

## 实验结果
- 女性编码声音更常被描述为顺从（p<.001）和性化（p<.001），男性编码声音更常被描述为支配（p<.001）和积极（p=0.0027）。
- 即使文本内容相同，这些差异仍然存在，表明声学特征（如韵律、副语言特征）起重要作用。
- 性别表达范围狭窄，几乎完全是二元和异性恋规范的。

## 一句话评价
该研究首次系统性地揭示了商业语音AI中合成声音的性别偏见，通过实验证明性化声音不仅反映社会刻板印象，还通过声学特征主动编码和放大性别权力不对称。

---

## 26. An Evaluation Framework for Text-to-Speech Voice Reconstruction

**作者**: Ariadna Sanchez, Christoph Minixhofer, Korin Richmond, Ondrej Klejch, Peter Bell, Simon King
**链接**: [2606.21343](https://arxiv.org/abs/2606.21343)
**分类**: Text-to-Speech | **关键词**: voice reconstruction, evaluation framework, best-worst scaling, distributional measure, text-to-speech, speaker similarity, intelligibility

## 核心痛点
现有语音重建评估依赖Mean Opinion Score (MOS)评估自然度和说话人相似性，但MOS存在灵敏度低、可靠性差、饱和等问题，无法很好地适配语音重建任务（即提高可懂度的同时保留说话人身份）。

## 方法创新
提出包含主观和客观两部分的新评估框架：
- **主观评估**：使用Best Worst Scaling (BWS)而非MOS，通过情境化任务（INTELLIGIBILITY和RECONSTRUCTION）让听者分别评估可懂度和说话人身份保留。
- **客观评估**：发现标准指标（WER、余弦相似度等）对严重不清晰说话人预测效果差，提出基于TTSDS2的双参考分布度量，同时衡量合成语音与高可懂度语音（可懂度）和原始不清晰语音（说话人身份）的距离。

## 实验结果
在193个说话人（四种言语障碍）、17个零样本TTS系统上进行评估。主观BWS结果显示：
- **可懂度**：StyleTTS2最高，Fish Speech次之，大多数系统优于原始录音。
- **重建质量**：IndexTTS2最高，Qwen3-TTS和E2-TTS次之。
框架验证了可靠性和任务对齐性。

## 一句话评价
该论文提出了一个针对语音重建任务的专用评估框架，克服了MOS的不足，主观和客观方法均与任务场景高度对齐。

---

## 27. Compiling Differentiable Audio Graphs to Real-Time DSP

**作者**: Facundo Franchino, Sebastian J. Schlecht
**链接**: [2606.21277](https://arxiv.org/abs/2606.21277)
**分类**: Audio DSP / Machine Learning Deployment | **关键词**: differentiable audio, compiler, real-time DSP, FAUST, feedback delay network, stability certificate, audible training, macro-controls

## 核心痛点
可微音频处理器通常在机器学习框架中设计和优化，但部署为实时音频效果仍需手动用专用DSP语言重写，过程易错、耗时，且将研究原型与生产工具分离。

## 方法创新
提出**ADAC**（自动可微音频编译器），其流程为：遍历训练模型的计算图 -> 提取参数 -> 降级为与框架无关的JSON中间表示 -> 生成等价的FAUST代码。支持拓扑：串联、并联、递归。关键特性包括：
- **可听训练**：每个梯度步后替换运行插件中的模型，使优化过程可听。
- **宏控制**：提供混响时间、干湿比、预延迟等参数，且保持稳定性。
- **稳定性证书**：根据小增益定理分析循环稳定性，在构建插件前验证导出的参数。
- **部署管道**：单次调用完成代码生成、认证、JUCE项目生成、编译和安装。

## 实验结果
- 以反馈延迟网络（FDN）为案例，编译的FAUST代码与源模型的脉冲响应差异在单精度浮点噪声范围内（峰值偏差<7e-5）。
- 32线FDN在Apple M2上运行约为实时90倍，64线为14倍。
- 混响时间控制实测（0.5s设置）与理论一致。
- 稳定性证书检测到正交矩阵的单精度瑕疵（σ_max=1.00000017）。

## 一句话评价
ADAC弥合了可微音频模型与实时DSP部署之间的鸿沟，通过编译器自动生成高效、稳定、可微调的FAUST代码，并支持可听训练和端到端部署。

---

## 28. Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach

**作者**: Tzu-Chieh Wei, Yi-Cheng Lin, Huang-Cheng Chou, Kuan-Yu Chen, Hsin-Yen Sung, Shrikanth Narayanan, Hung-yi Lee
**链接**: [2606.21215](https://arxiv.org/abs/2606.21215)
**分类**: Speaker Verification | **关键词**: speaker verification, non-verbal vocalizations, mixture of experts, knowledge distillation, self-supervised learning

# 论文总结

## 核心痛点
- 当前说话人验证（SV）系统在非语言发声（NVV）上泛化能力差。
- 直接微调会导致灾难性遗忘，严重降低语音验证性能。

## 方法创新
- 提出**条件蒸馏与混合专家（MoE）框架**：
  - 使用冻结的Data2Vec自监督特征 + ECAPA-TDNN骨干。
  - 插入MoE模块，通过领域感知路由分离语音和NVV处理路径。
  - 设计**条件蒸馏损失**（仅对语音样本应用）以保持语音性能。
  - 引入**监督对比损失**缩小语音-NVV域差距。
  - 事件引导的路由约束（负载均衡、类内一致性、类间分离）。
- 两种MoE集成策略：后融合MoE和层间残差MoE（IR-MoE）。

## 实验结果
- 在NonverbalTTS数据集上（10种NVV类型），NVV vs 语音EER从38.93%降至22.66%，语音EER从13.17%降至9.24%。
- IR-MoE优于后融合MoE，4专家配置最优。

## 一句话评价
首个对10种NVV类型进行系统评估的研究，提出的条件蒸馏与MoE方法有效兼顾了NVV和语音验证性能的提升。

---

## 29. Noise-Driven Instrument Based on Coherent Quantum and Stochastic Oscillator Models

**作者**: Felipe Gonzalez de la Maza, Maciej Lewenstein, Antoine Reserbat-Plantey, Reiko Yamada
**链接**: [2606.20690](https://arxiv.org/abs/2606.20690)
**分类**: Electroacoustic Instrument Design | **关键词**: Electroacoustic instrument, Quantum harmonic oscillator, Stochastic string excitation, Nonlinear dynamics, Noise-driven excitation, Open-loop actuation

## 核心痛点
传统电磁驱动弦乐器多采用闭环反馈或确定性激励（如正弦波），导致音色稳定但频谱稀疏，缺乏复杂性和变化性。

## 方法创新
本文提出一种开环随机激励范式：使用白噪声信号直接驱动电磁线圈，无反馈、无相位锁定、无音高控制。通过定制电磁线圈（8Ω直流电阻、~255匝、钕磁铁增强），实现宽带随机磁场激发琴弦振动。同时，通过优化线圈磁场聚焦和空间布局，降低电磁串扰。

## 实验结果
频谱对比显示：传统拨弦产生清晰基频和离散谐波；随机激励产生密集、均匀分布的谱峰，能量更平坦，音色更复杂丰富。

## 一句话评价
成功将量子谐振子与经典随机振子的相空间类比转化为可听的声学现象，为量子启发乐器设计提供了新颖的物理实现平台。

---

## 30. From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection

**作者**: Jan Jasiński, Mateusz Barański, Julitta Bartolewska, Marcin Witkowski, Konrad Kowalczyk
**链接**: [2606.23060](https://arxiv.org/abs/2606.23060)
**分类**: Automatic Speech Recognition (ASR) Hallucination Detection | **关键词**: Whisper large v3, hallucination detection, text metrics, LLM, internal state probing, meta-classifier, reference-free detection

# 论文总结

## 核心痛点
ASR模型（尤其是Whisper large v3）会产生流畅但无语音基础的幻觉转录，传统指标（如WER）无法有效区分幻觉与其他错误，且多依赖参考文本，限制了实际部署。缺乏真实语音的人类注释数据进一步阻碍了检测方法验证。

## 方法创新
1. **文本指标检测**：系统评估了有参考和无参考文本特征，使用随机森林和XGBoost等树模型融合特征，显著优于线性基线；但无参考特征性能严重下降。
2. **LLM检测**：通过提示工程注入Whisper特定幻觉知识（如非语音音频常见短语）和少样本示例，提升了LLM（GPT-4o mini, Gemini Flash）的F1分数，但仍未超越轻量文本分类器。
3. **内部解码器状态探针**：从Whisper解码器中间层提取表示，无需参考文本即可检测幻觉，表现最强；使用完整解码序列优于单token嵌入。
4. **跨范式融合**：设计元分类器结合文本与内部状态输出，利用二者互补信号，达到最佳整体性能。

## 实验结果
- 综合文本特征（有参考）XGBoost F1=62.8%；无参考时F1=37.7%。
- LLM最佳（有参考）F1=58.7%（Gemini Flash 3.0 + 领域知识 + 少样本）；无参考时F1=32.8%。
- 内部状态探针无参考AUC达80%以上，优于所有无参考方法。
- 融合元分类器F1=68.9%，为最高。

## 一句话评价
本文系统对比了三种ASR幻觉检测范式，发现内部解码器状态探针结合后期融合是当前最有效的无参考检测方案，为实际部署提供了方向。

---

## 31. HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems

**作者**: Mateusz Barański, Jan Jasiński, Julitta Bartolewska, Marcin Witkowski, Konrad Kowalczyk
**链接**: [2606.23048](https://arxiv.org/abs/2606.23048)
**分类**: Automatic Speech Recognition | **关键词**: hallucination, ASR, human-annotated dataset, benchmark, error detection

### 核心痛点
当前ASR系统的幻觉检测方法多基于非语音或人工损坏音频，缺乏对自然语音中真实幻觉的研究和标准化基准。

### 方法创新
- 构建首个真实语音幻觉人工标注数据集HALAS，包含7种SOTA ASR模型在Earnings 22录音上的span级标签。
- 利用模型间WER差异选择高难度音频片段，提高幻觉比例。
- 提供训练/测试划分，支持幻觉检测方法的评估。

### 实验结果
- 所有模型均出现幻觉，平均幻觉率30.9%，但仅有1.1%循环。
- 幻觉短语分布高度集中：平均55%的幻觉属于前10个常见短语。
- 现有检测方法（基于字符/语义指标）ROC-AUC达81%，而SOTA检测F1仅53.1%。

### 一句话评价
HALAS是首个针对真实语音ASR幻觉的人工标注数据集，揭示了现有检测方法的不足，为幻觉缓解研究提供了可靠基准。

---

## 32. Interleaved Speech Language Models Latently Work In Text

**作者**: Talia Sternberg, Gallil Maimon, Yossi Adi
**链接**: [2606.22473](https://arxiv.org/abs/2606.22473)
**分类**: Speech Language Models - Mechanistic Interpretability | **关键词**: Interleaved Speech-Text LMs, Implicit Latent Transcription, Logit Lens, Factual Knowledge, Mechanistic Interpretability

## 核心痛点
当前语音语言模型（SLM）在语义和知识能力上存在不足，而引入文本数据和预训练文本语言模型（如交错语音-文本训练）虽能提升性能，但其内部机制尚不明确。

## 方法创新
本文使用**logit lens**方法分析交错SLM的中间层表示，发现模型在未专门训练语音识别的情况下，会隐式地将语音表示转录为对应文本（隐式转录），并在文本空间中进行后续推理，最后再映射回语音空间。通过最大池化聚合语音token位置的logits，追踪模态偏好和转录准确性。

## 实验结果
1. **隐式转录普遍存在**：在多种模型家族和规模中，中间层解码出的文本转录出现在top-k候选词中的比例高达77%。
2. **必要条件**：文本LM初始化与交错训练数据二者缺一不可，仅语音训练或随机初始化无法产生该现象。
3. **知识能力关联**：隐式转录的强度与模型从语音中检索事实知识的能力正相关，但不能完全解释该能力。
4. **定性分析**：转录过程逐步构建，有时包含声学错误。

## 一句话评价
首次揭示了交错语音-文本LM在内部隐式地将语音转写为文本并进行推理的机制，为优化SLM提供了新的理解视角。

---

## 33. Towards Accurate and Robust Surveillance Roadside IVD via Trackletized Audio-Visual Reasoning

**作者**: Xiwen Li, Xiaoya Tang, Bodong Zhang, Tolga Tasdizen
**链接**: [2606.22299](https://arxiv.org/abs/2606.22299)
**分类**: Audio-Visual Learning / Vehicle Detection | **关键词**: Idling Vehicle Detection, Audio-Visual Fusion, Multi-Object Tracking, Tracklet, Contrastive Learning, Domain Generalization, Surveillance

## 论文总结

### 核心痛点
现有的端到端IVD方法（如AVIVDNet、HAVT-IVD）依赖于全帧、片段级别的融合，容易过拟合场景背景和全帧上下文，产生不稳定的时间决策，缺乏明确的先验来对齐车辆与麦克风，导致在域漂移下脆弱且数据效率低。

### 方法创新
提出TAVR-IVD框架，基于多目标跟踪的音频-视觉推理：
- **实例锚定**：通过目标检测和跟踪构建车辆轨迹（tracklet），将问题从全帧分类转为每条轨迹的跨模态推理。
- **几何条件绑定（MASP）**：利用车辆几何信息（轨迹位置、位移）作为空间先验，从全局混合多声道音频中归因到具体车辆。
- **轨迹条件分类器**：沿轨迹聚合多模态证据，产生稳定的逐车状态预测。
- **JACE模块**：通过监督对比学习构建状态结构化的跨模态潜在空间，减少捷径学习，增强域鲁棒性。
- **新数据集**：构建AVIVD-LT（同地不同天）和AVIVD-M（不同站点）评估集，测试跨天和跨站点泛化。

### 实验结果
在AVIVD验证集及新构建的测试集上取得SOTA，证明高精度和更好的域迁移鲁棒性。

### 一句话评价
通过轨迹级音频-视觉推理，显著提升路边车辆怠速检测的准确性和跨域泛化能力。

---

## 34. Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study

**作者**: Tomoki Koriyama
**链接**: [2606.22009](https://arxiv.org/abs/2606.22009)
**分类**: Text-to-Speech | **关键词**: grapheme-to-phoneme, large language model, Japanese, benchmark, text-to-speech

### 核心痛点
日语G2P转换面临独特挑战：无词边界、汉字多音、数词不规则发音等。传统规则系统（如OpenJTalk、MeCab）依赖词典，对未登录词和特殊读法处理有限。

### 方法创新
1. **Parse Mode**：LLM执行形态分析（分词+读音估计），后接规则后处理（助词转换、长音规范化），分离LLM与确定性规则。
2. **Direct Mode**：LLM直接预测整句片假名读音，需处理全部发音规则。
评估30+模型（API和开源），并与传统工具对比。

### 实验结果
- 模型规模、版本、日语专门训练是关键因素。
- 最佳LLM（parse mode）的字符错误率（CER）低于0.52%，传统工具最优为1.03%。
- Parse mode在大多数模型上优于direct mode。
- 将LLM预测的kana输入kana-input TTS，发音准确性优于端到端TTS。

### 一句话评价
首个大规模日语G2P基准，证明LLM结合规则后处理可显著超越传统方法。

---

## 35. Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR

**作者**: Enes Yavuz Ugan, Alexander Waibel
**链接**: [2606.21990](https://arxiv.org/abs/2606.21990)
**分类**: Speech Recognition | **关键词**: Code-switching, Multilingual ASR, Bayesian Low-Rank Adaptation, Whisper, Synthetic Data, Knowledge Integration

### 核心痛点
当前的强多语言ASR模型（如Whisper）在微调合成代码切换（CSW）数据时，会显著退化单语言性能（例如，标准LoRA微调导致德语WER相对增加418%）。因此，如何在不损害已有能力的前提下提升代码切换鲁棒性是一个重要挑战。

### 方法创新
提出**贝叶斯因子化适应（Bayesian Low-Rank Adaptation, BLoRA）**，通过引入贝叶斯先验，学习稀疏且含不确定性的适配矩阵，使模型仅修改与切换相关的少量权重，从而在不覆盖原始知识的前提下有效集成新知识。该方法仅需少量合成数据（LLM生成代码切换文本 + TTS拼接语音），无需真实代码切换语音。

### 实验结果
- 在CSFleurs基准上，代码切换词的点兴趣错误率（PIER）相对降低 **32.87%**，整体WER提升 **5.31%**。
- 在CommonVoice上单语言性能保持稳定，无退化。
- 对比实验表明：数据复杂度不如知识集成方式重要，单纯增加合成数据量或复杂度无法解决问题。

### 一句话评价
提出一种无需真实代码切换数据、可扩展的强模型适应方法，通过贝叶斯稀疏适配有效平衡代码切换能力与单语言性能。


---

## 36. Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems

**作者**: Jingjing Jiang, Atsumoto Ohashi, Ryuichiro Higashinaka
**链接**: [2606.21970](https://arxiv.org/abs/2606.21970)
**分类**: Spoken Dialogue System, Full-duplex Multimodal Interaction | **关键词**: spoken dialogue system, full-duplex, multimodal interactions, face generation, VQ-VAE

## 核心痛点
现有全双工口语对话系统（如Moshi）仅处理音频模态，缺乏面部表情、唇动、头部运动等非语言线索，无法模拟真实人类对话的多模态同步性。

## 方法创新
- **Face Codec**：采用VQ-VAE将3D FLAME面部网格（25fps）压缩为离散面令牌（12.5Hz，N=8），与Moshi的音频令牌帧率对齐。
- **Moshi-Face架构**：在Moshi的基础上扩展Face Transformer模块，通过非自回归方式并行生成N个面令牌，利用RQ-Transformer的隐藏状态和文本/音频嵌入作为条件。
- **训练策略**：两阶段训练——先训练Face Codec，再冻结或微调整个模型，并引入教师强制以保持时序一致性。

## 实验结果
- 在约180小时对话数据（Seamless Interaction Dataset）上训练，基于Moshi（7B参数）和VHAP提取3D网格。
- Face Codec在codebook大小256、嵌入维度128时达到最优性能：MVE=9.90×10⁻³，LVE=11.77×10⁻³，困惑度0.66。
- Moshi-Face实现低延迟音视频同步，且对话质量与原始纯音频模型相当（具体指标未展示，但论文声称保持质量）。

## 一句话评价
Moshi-Face是首个实现全双工多模态口语对话的模型，成功将实时面部生成集成到对话系统中，在低延迟下实现音视频对齐。

---

## 37. AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation

**作者**: Dongmei Wang, Xiaohang Sun, Yang Liu, Fanjie Kong, Abhishek Yanamandra, Abhinav Jain, Daniel Tompkins, Woohyun Kang, Najmeh Sadoughi, Sunil Hadap, Xiang Hao, Zhu Liu, Caren Chen
**链接**: [2606.21893](https://arxiv.org/abs/2606.21893)
**分类**: Speech Coding | **关键词**: neural speech codec, low-bitrate, disentangled representation, data augmentation, semantic tokens, speaker tokens, prosody tokens, AugCodec

## 核心痛点
现有的神经语音编解码器在低比特率下难以同时实现高质量重建和有效的特征解耦（语义、说话人、韵律），且常依赖多层级残差量化导致高帧率，或解耦不彻底导致特征混淆。

## 方法创新
1. **数据增强驱动的解耦策略**：通过三种定制化输入变体分别提取语义（语音转换后的语音）、说话人（同说话人不同话语）、韵律（低频谱STFT）特征，从源头分离信息，避免交叉干扰。
2. **压缩与扩展机制**：语义编码器采用帧拼接与线性投影实现时间压缩（降低帧率），解码时通过分段线性投影恢复细节；韵律编码器使用更粗的帧率（160ms）以匹配长时特征。
3. **增强损失**：对齐原始语音与语音转换后的语义编码器输出，促进说话人无关语义学习并缓解转换带来的声学失配。
4. **低帧率设计**：最终仅使用12.5Hz的三流token（语义、说话人、韵律），无需残差量化。

## 实验结果
在LibriSpeech test-clean上，AugCodec在重建质量（如PESQ、STOI）和语义保持（WER）方面显著优于FACodec、FreeCodec等基线，同时以12.5Hz的超低帧率运行，展示了优良的解耦能力与压缩效率。

## 一句话评价
AugCodec通过精巧的数据增强实现了高效的低比特率解耦语音编解码，为语音压缩与下游任务提供了紧凑且分离的表征。

---

## 38. Improving Engine Sound Analysis in Hot-Test Environments via a RAB-U-Net (Residual Attention Block U-Net) Noise Removal Method

**作者**: Raheleh Mohseni, Mahdi Alyari
**链接**: [2606.21887](https://arxiv.org/abs/2606.21887)
**分类**: Audio Enhancement | **关键词**: Engine sound, Environmental noises, Deep learning, U-Net, RAB-U-Net, Noise removal

## 核心痛点
在发动机生产线热测试中，背景噪声严重干扰声音分析，导致传统人工检测和现有AI系统诊断准确率下降，易遗漏故障并引发客户投诉。

## 方法创新
提出RAB-U-Net（Residual Attention Block U-Net），在标准U-Net中集成残差块和注意力机制，以改进特征提取、缓解梯度消失、聚焦重要声学区域，从而有效去除发动机声音中的环境噪声。

## 实验结果
在真实工厂环境数据集上，RAB-U-Net相比传统滤波、小波去噪及标准U-Net等方法，显著降低噪声残留，提升故障检测准确率，具备实时应用潜力。

## 一句话评价
一项针对工业噪声环境的创新深度学习降噪方案，通过残差注意力增强U-Net，有效提升发动机热测试诊断可靠性。

---

## 39. Gradient-Based Learning of Parametric Engine Sound Representations for Real-Time Resynthesis and Tuning on Embedded Systems

**作者**: Robin Doerfler, Matthieu Kuntz, Clemens Zimmer
**链接**: [2606.21521](https://arxiv.org/abs/2606.21521)
**分类**: Audio Synthesis / Engine Sound Modeling | **关键词**: engine sound synthesis, engine order enhancement, analysis-by-synthesis, differentiable digital signal processing, parametric sound representation, neural audio synthesis, active sound design, embedded audio systems

## 核心痛点
传统发动机声音合成（如Engine Order Enhancement）在逼真度和可调性之间存在权衡，且难以同时建模谐波和噪声成分。现有神经音频合成方法虽然逼真度高，但难以集成到现有嵌入式EOE框架中。

## 方法创新
提出**EONE模型**，通过端到端可微的分析-合成方法学习发动机声音的紧凑参数表示。核心创新包括：
1. **因子化RPM-扭矩增益曲线**：将每个谐波和噪声带的幅度分解为RPM和扭矩的独立一维函数（乘法组合），减少参数并保持可调性。
2. **可微合成路径**：将参数优化转化为梯度下降问题，避免传统DSP分析的歧义。
3. **预训练-微调策略**：先在大规模发动机录音上预训练Timbre Encoder-Decoder学习隐空间，再在目标录音上微调增益曲线，实现鲁棒泛化。
4. **与现有EOE框架兼容**：学习的参数可直接映射到传统DSP实现，部署于嵌入式系统（如EVx Suite）。

## 实验结果
频谱指标（如MRSTFT）和听力测试表明，尽管压缩为紧凑参数表示（40个点/曲线），重建保真度仍足够高。在EVx Suite上的集成验证了技术可行性。

## 一句话评价
一种兼顾逼真度、可调性和嵌入式部署可行性的发动机声音参数化学习框架。

---

## 40. DisSpeech: Low-Resource Controllable Mandarin Stuttered Speech Synthesis for ASR Augmentation

**作者**: Yao Lu
**链接**: [2606.21457](https://arxiv.org/abs/2606.21457)
**分类**: Speech Synthesis and ASR Augmentation | **关键词**: Stuttered speech synthesis, Controllable speech generation, ASR data augmentation, Mandarin stuttered speech, Low-resource speech synthesis, Discrete speech tokens, Masked generative Transformer

## 核心痛点
- 普通话口吃语音数据稀缺，现有ASR模型对口吃语音识别性能显著下降。
- 现有口吃语音合成方法（如Stutter-TTS）生成不稳定，约20%样本不可听，且主要针对英语。

## 方法创新
- 提出DisSpeech框架，基于离散语义语音token（SpeechTokenizer的RVQ1层）作为中间表示。
- 采用非自回归掩码生成Transformer（类似MaskGCT）从文本和显式口吃事件标签（重复、延长、阻塞）预测语义token序列。
- 引入韵律感知声学解码器，显式建模音高和能量的时间变化，提升自然度。
- 仅需不到50小时的普通话口吃语音进行微调，实现低资源可控生成。

## 实验结果
- 在语音质量和事件可控性上优于Stutter-TTS等基线方法。
- 合成的口吃语音用于数据增强，一致提升多个ASR模型（如Qwen3-ASR-0.6B）的识别性能，CER降至4.19%，达到SOTA。
- 增强后ASR模型对流畅语音的性能仅有轻微下降。

## 一句话评价
DisSpeech通过离散token表示与非自回归生成策略，在低资源条件下实现了高质量、可控的普通话口吃语音合成，并有效提升了ASR系统的鲁棒性。

---

## 41. CORTIS: Text-Only Adaptation of Spoken Language Models for Task-Oriented Voice Agents

**作者**: Youngwon Choi, Hyeonyu Kim, Taeyoun Kwon, Donghyuk Jung, Myeongkyun Cho
**链接**: [2606.21453](https://arxiv.org/abs/2606.21453)
**分类**: Spoken Language Understanding / Task-Oriented Voice Agents | **关键词**: spoken language model, text-only adaptation, task-oriented voice agents, structured output generation, instruction tuning, ASR-LLM cascade, noise robustness

## 论文总结

### 核心痛点
任务型语音助手需要将用户语音映射到结构化输出（如语义框架、函数调用）。传统ASR-LLM级联方法受限于ASR转录错误，尤其在噪声环境下会传播至下游任务。而口语语言模型（SLM）可直接处理语音，但其适应新任务通常需要配对的语音-目标标注数据，收集成本高昂。

### 方法创新
CORTIS提出一种纯文本适应框架：仅使用文本形式的任务监督数据（指令-结构化输出对）微调SLM中的LLM组件，同时冻结语音编码器和模态适配器。通过保持训练时文本查询与推理时语音查询在提示模板中的位置一致，利用SLM预训练的语音-文本对齐能力，使模型在推理时直接从语音生成结构化输出。方法无需任务特定的语音-目标配对数据。

### 实验结果
基于Qwen2.5-Omni骨干，在FSC、SLURP及内部产品数据集上评估。与使用相同文本监督训练的ASR-LLM级联相比，CORTIS在干净语音下表现相当，在噪声（babble噪声）条件下尤其在高层任务语义保持上优势更明显。表明纯文本微调SLM是一种实用的语音助手适应策略。

### 一句话评价
CORTIS通过纯文本监督微调SLM，有效避免了ASR级联的误差传播，且无需昂贵的语音标注，在噪声环境下展示了更好的语义鲁棒性。

---

## 42. SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion

**作者**: Hounsu Kim, Juhan Nam
**链接**: [2606.21157](https://arxiv.org/abs/2606.21157)
**分类**: Speech Codec | **关键词**: speaker decoupling, low-bitrate coding, zero-shot voice conversion, pitch injection, neural speech codec

## 核心痛点
现有说话人解耦编解码器面临权衡：显式抑制说话人泄漏的方法（如梯度反转、扰动）训练复杂且不稳定，而简单设计（如BiCodec）可能导致局部token中残留说话人信息。同时，低比特率编解码器多依赖文本对齐、可变帧率或生成式解码器，引入额外假设或牺牲重建保真度。

## 方法创新
SDP-Codec提出一种单阶段训练的说话人解耦、音高注入编解码器：
1. **局部流**：使用vq-wav2vec的连续预量化特征（而非离散单元），通过小码本（300或1536条目）强制瓶颈以去除说话人信息；
2. **音高注入**：提取归一化F0，通过音高编码器-解码器（含全局条件去归一化）注入局部流，并采用软标签音高重建损失（360 bin cent直方图与高斯模糊目标）提供平滑梯度；
3. **全局流**：基于WavLM特征通过感知器重采样器生成固定长度说话人嵌入，通过位置无关交叉注意力和自适应蛇形激活抑制局部信息；
4. **训练目标**：多尺度mel L1损失、承诺损失、LSGAN对抗损失+特征匹配损失、软标签音高重建损失。

## 实验结果
- **重建性能**：在16kHz和24kHz设置下，SDP-Codec在UTMOS、SECS、F0相关性等指标上优于或接近LSCodec、XCodec等基线，尤其在说话人相似度（SECS）上表现突出（16kHz小模型0.9372，大模型0.9436）。
- **零样本语音转换**：在16kHz大模型（SDP-Codec-16-L）上，SECS达0.8405，F0相关性0.6088，显著高于BiCodec和MSRCodec，且说话人探测准确率最低（未给出具体数值，但文中提“lowest speaker-probing accuracy”）。
- **比特率**：小模型0.45 kbps，大模型0.52 kbps，与主流低比特率编解码器相当。

## 一句话评价
SDP-Codec通过单阶段流水线结合音高注入与紧凑码本，在极低比特率下实现高质量重建和强零样本语音转换，同时有效减少说话人泄漏。

---

## 43. A Generalized Formalism of Auto-Regressive Decoding for Speech Processing

**作者**: Julia Gachot, Philipp Allgeuer, Marie S. Bauer, Stefan Wermter
**链接**: [2606.20714](https://arxiv.org/abs/2606.20714)
**分类**: Speech Processing | **关键词**: Auto-regressive decoding, Speech processing, Decoding strategy, Formalism, Sequence prediction

## 核心痛点
语音处理中自回归解码策略缺乏统一的形式化框架，导致策略选择、比较和评估困难。现有定义隐式且多样，存在不一致性；搜索策略常被视为实现细节，缺少系统分类和基准测试。

## 方法创新
提出一种广义的自回归解码形式化框架，将AR策略视为由四个模块化步骤（估计、决策、先验更新、终止测试）组成的迭代过程。该框架基于SIPC（随机整数概率约束问题）形式化，明确定义AR预测器的包含标准，并支持确定性/随机策略的统一描述。

## 实验结果
论文未提供具体实验，但展示了框架在消融研究中的潜力，能够隔离每个步骤的贡献。

## 一句话评价
该工作为理解、比较和设计语音处理中的AR解码策略提供了首个系统化形式化工具。

---

## 44. MindAlign: Decoding Inner Speech from fMRI Signals via Multimodal Embedding Alignment under Limited Data

**作者**: Muxuan Liu, Ichiro Kobayashi, Satoshi Nishida
**链接**: [2606.20696](https://arxiv.org/abs/2606.20696)
**分类**: fMRI-based Language Decoding / Inner Speech Decoding | **关键词**: fMRI, Inner Speech, Multimodal Embedding Alignment, Soft Prefix Tuning, Brain-to-Text, Cross-Subject Generalization

## 核心痛点
- 缺乏可观测的言语输出，数据有限，跨被试差异大
- 现有方法依赖任务特定解码器微调，可扩展性差

## 方法创新
- 提出MindAlign两阶段框架：Stage1学习被试特异性神经-语义对齐，将fMRI映射到多模态语义空间（以CLIP视觉嵌入为中间监督）；Stage2通过软前缀提示将语义草图与图像特征融合，输入冻结的LLaVA模型生成自由文本
- 无需外部音频-词元对齐，支持跨被试泛化
- 引入类别内混合（Intra-category Mixup）和空间约束噪声注入增强鲁棒性

## 实验结果
- 在5名被试约2000个样本的静默图像描述fMRI数据上，生成流利日语文本，显著优于仅fMRI和随机基线
- 跨被试实验表明，学得的语义到语言投影可泛化

## 一句话评价
MindAlign提供了一种可扩展、模块化的脑到文本解码方案，首次实现有限数据下从fMRI解码内心言语的自由生成。

---

## 45. Beyond ROC-AUC: Operating-Point Performance Reporting for Biometric Verification

**作者**: Ajan Ahmed, Masudul H. Imtiaz
**链接**: [2606.20680](https://arxiv.org/abs/2606.20680)
**分类**: Biometric Verification | **关键词**: ROC-AUC, operating point, detection error tradeoff, biometric verification, ISO/IEC 19795, false match rate, false non-match rate, confidence intervals, bootstrap

# 论文总结：Beyond ROC-AUC: Operating-Point Performance Reporting for Biometric Verification

## 核心痛点
当前生物特征验证领域普遍使用ROC-AUC、EER或验证准确率作为全局指标，但ISO/IEC 19795-1标准推荐在特定操作点（如低FMR）报告性能。全ROC-AUC在[0,1]的FMR范围内等权平均，而实际部署仅关注低FMR区间（如10^-3），导致全局指标可能掩盖低FMR性能甚至颠倒系统排名。

## 方法创新
论文重新审视ISO/IEC 19795-1标准，强调以DET曲线和固定FMR下的FNMR为主要报告指标，辅以部分AUC、log-FMR AUC、最小检测成本等，并建议使用bootstrap置信区间和配对检验来量化不确定性。实验覆盖人脸、语音、虹膜和指纹四种模态，涉及七个预训练匹配器，验证了全ROC-AUC与操作点性能的差异。

## 实验结果
以人脸为例，FaceNet获得更高的全ROC-AUC，而ArcFace在FMR=10^-3下获得更高的TMR，且差距显著（置信区间不重叠）。这表明根据全ROC-AUC和操作点性能会得到不同的系统排名。其他模态也有类似现象。

## 一句话评价
该论文有力地论证了生物特征验证中应弃用全ROC-AUC作为主要指标，转向操作点导向的标准化报告，并提供了实证和检查清单。

---

## 46. EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis

**作者**: Minghui Wu, Ganjun Liu, Zikun Fang, Ting Meng, Hongchuan Wu, Bingao Xu, Yonglong Cai, Jiasheng Chen, Jun Du
**链接**: [2606.20650](https://arxiv.org/abs/2606.20650)
**分类**: Text-to-Speech | **关键词**: Emotional Speech Synthesis, Instruction-Guided TTS, Emotion2embed, Flow-Based Modeling, Dual-Path Control

## 核心痛点
现有的指令可控语音合成方法通常依赖粗粒度的情感标签，缺乏对细粒度情感强度（如低、中、高）的显式建模，导致情感控制不稳定，且语言指令难以捕获详细的声学情感关联。

## 方法创新
提出**EmoInstruct-TTS**，一种**双路径指令引导框架**，结合自然语言语义指导与结构化情感嵌入实现细粒度情感调制。具体包括：
- **Emotion2embed**：一种监督式语义-声学情感嵌入，覆盖48种情感状态（27个细粒度类别+7种基本情绪×3个强度等级共21个情绪-强度组合），通过多任务学习（分类+排序）保持强度顺序结构。
- **ICE-Flow**：指令条件情感流模型，将自由形式的自然语言指令映射到声学基础的情感嵌入，采用样本级监督和分布级正则化防止模式塌陷。
- **双路径合成**：将LLM语义规划（路径1）与显式情感嵌入控制（路径2）分离，通过LLM生成语义token，结合情感嵌入和说话人嵌入，由CFM TTS和BigVGAN生成波形。

## 实验结果
- 在ESD和CNCED数据集上进行零样本主观评估（MOS、ESMOS、SSMOS），EmoInstruct-TTS在情感可控性和自然度上优于CosyVoice2/3基线。
- 消融实验验证了双路径（指令+情感嵌入）的互补性：单独使用文本指令或情感嵌入均导致性能下降。
- 嵌入分析显示ICE-Flow生成的情感嵌入保持类别紧凑性和强度排序（PCS=0.67, VR=0.96, IOA=0.91）。

## 一句话评价
EmoInstruct-TTS通过双路径结构将语义规划与细粒度情感控制分离，有效提升了指令驱动情感语音合成的可控性和自然度。


---

