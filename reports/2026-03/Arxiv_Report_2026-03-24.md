# Arxiv Daily Deep Report - 2026-03-24

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 15
---

## 1. SelfTTS: cross-speaker style transfer through explicit embedding disentanglement and self-refinement using self-augmentation

**作者**: Lucas H. Ueda, João G. T. Lima, Pedro R. Corrêa, Flávio O. Simões, Mário U. Neto, Paula D. P. Costa
**链接**: [2603.22252](https://arxiv.org/abs/2603.22252)
**分类**: Text-to-Speech | **关键词**: text-to-speech, cross-speaker style transfer, synthetic data, self-augmentation, disentanglement, representation learning

# 核心痛点
跨说话者风格转换中，现有方法常出现说话者泄漏问题，即参考说话者的音色被错误捕获，导致身份不匹配和性能下降。此外，需要外部预训练说话者或情感编码器，且高质量表达性数据稀缺，限制了模型的应用和自然度。

# 方法创新
SelfTTS提出以下创新点：
1. **多正对比学习（MPCL）损失**：用于诱导说话者和情感嵌入的聚类表示，基于标签生成有效集群，无需复杂批处理流程。
2. **显式嵌入解缠**：结合梯度反转层（GRL）和余弦相似度损失，直接作用于说话者和情感嵌入，去除重叠信息，确保鲁棒的跨说话者风格转换。
3. **自我增强策略**：利用模型基于VITS架构的固有语音转换能力，通过自我增强生成合成数据，提升合成语音的自然度，同时保持情感表达和目标音色。

# 实验结果
实验结果表明，SelfTTS在情感自然度（eMOS）和稳健稳定性（目标音色和情感）方面优于最先进的基线模型。评估包括跨语料库实验，使用公开数据集和代码验证了方法的有效性。

# 一句话评价
SelfTTS是一个创新的文本到语音模型，通过有效的解缠和增强技术，显著提升了跨说话者风格转换的质量和自然度，无需依赖外部编码器。

---

## 2. WiRD-Gest: Gesture Recognition In The Real World Using Range-Doppler Wi-Fi Sensing on COTS Hardware

**作者**: Jessica Sanson, Rahul C. Shah, Yazhou Zhu, Rafael Rosales, Valerio Frascolla
**链接**: [2603.22131](https://arxiv.org/abs/2603.22131)
**分类**: Wi-Fi-based Gesture Recognition | **关键词**: Gesture Recognition, Wi-Fi, Monostatic Sensing, Full-duplex, Range-Doppler, COTS Hardware

# 核心痛点
现有Wi-Fi手势识别方法主要基于双基地传感，分析信道状态信息（CSI）模式，但缺乏精确空间信息（如距离），导致对环境变化、设备部署和多目标移动高度敏感。在控制环境中有效，但在真实世界、拥挤的公共场所中性能显著下降，无法区分前景手势和背景运动。

# 方法创新
WiRD-Gest提出一种新颖的单基地Wi-Fi传感系统，使用单个未修改的商用现成（COTS）设备（如笔记本电脑）提取Range-Doppler（RD）信息。关键创新包括：
- 全双工单基地管道，在单设备上实现自包含传感，无需硬件修改，同时保持正常Wi-Fi通信。
- 利用RD地图作为输入数据，提供空间维度信息，提高鲁棒性和泛化能力。
- 开发同步和自干扰消除算法，确保高保真RD估计。
- 首个基于RD数据的Wi-Fi单基地传感深度学习基准，评估多种模型（如CNN2D+RNN/GRU/LSTM、3D CNN、Video Transformers）。

# 实验结果
- 在控制环境中收集数据集，包含五种手势（推拉、滑动、上下、双击、双旋转），涉及五个用户，总样本数约191,000帧。
- 模型在域内测试（随机分割）、跨用户测试（留一用户出）和不可见公共空间测试（咖啡馆）中表现优异。
- 在拥挤的公共环境中，即使有动态干扰和背景移动目标，系统性能仅轻微下降，而现有方法往往失败。
- 发布开源数据集和基准，促进可重复研究。

# 一句话评价
WiRD-Gest是首个在COTS设备上实现单基地Wi-Fi手势识别的实用系统，通过引入空间信息，显著提高了在真实世界环境中的准确性、鲁棒性和泛化能力。

---

## 3. Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations

**作者**: Xin Guo, Chunrui Zhao, Hong Jia, Ting Dang, Gongping Huang, Xianrui Zheng, Yan Gao
**链接**: [2603.21888](https://arxiv.org/abs/2603.21888)
**分类**: Speech Processing | **关键词**: Federated learning, Self-supervised learning, Speech processing, Early exit, Heterogeneous system, Model adaptation

# 详细总结

## 核心痛点
联邦学习（FL）与自监督学习（SSL）结合用于语音任务微调时，面临显著异构性挑战：系统异构性（客户端计算能力差异大，导致straggler效果和资源浪费）和任务异构性（下游语音任务如自动语音识别和关键词检测需要不同表示深度，统一全模型更新效率低下）。

## 方法创新
- **自适应早期退出框架**：在预训练SSL骨干（如Wav2Vec 2.0）的中间Transformer层（如第3、6、9、12层）插入轻量级任务特定预测头，使客户端能基于本地计算资源和任务复杂度选择退出点，提前终止训练或推理。
- **资源和任务感知本地训练**：每个客户端动态确定最大可训练深度，结合硬件约束（如内存容量）和任务需求，优化计算效率。
- **层级深度感知部分聚合**：服务器采用层级的、深度加权的部分聚合策略，独立聚合每一层的更新，仅聚合训练了该层的客户端，权重基于本地数据大小和最大训练深度，以缓解异构性影响。

## 实验结果
在五个下游语音任务上评估：自动语音识别（ASR，LibriSpeech）、关键词检测（KWS，Google Speech Commands）、情感识别（ER，IEMOCAP）、说话人识别（SID）和自动说话人验证（ASV，VoxCeleb1）。使用Wav2Vec 2.0 Base作为骨干，实验设置包括集中式训练、同质联邦学习和异质联邦学习场景。结果表明，框架在资源约束的联邦环境中显著减少计算开销，支持异构硬件，并在保持竞争性能的同时优化收敛。

## 一句话评价
该研究通过创新的自适应早期退出和层级聚合机制，有效平衡了联邦语音学习中的效率与性能，为异构环境下的隐私保护微调提供了实用解决方案。

---

## 4. Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

**作者**: Xi Xuan, Wenxin Zhang, Zhiyu Li, Jennifer Williams, Ville Hautamäki, Tomi H. Kinnunen
**链接**: [2603.21875](https://arxiv.org/abs/2603.21875)
**分类**: Speech Deepfake Verification | **关键词**: speaker disentanglement, deepfake source verification, Chebyshev polynomial, Riemannian geometry

# 核心痛点
现有语音深度伪造源验证系统通常假设源嵌入独立于说话人特征，但此假设未经验证。说话人特征与合成痕迹纠缠，导致模型依赖说话人线索而非源证据，引发捷径学习，降低了源验证的鲁棒性和泛化能力。

# 方法创新
论文提出一个说话人解缠度量学习（SDML）框架，集成两种新颖损失函数：
- **ChebySD-AAM**：基于切比雪夫多项式近似，解决标准AAM-Softmax的梯度不稳定问题，并引入阈值化说话人自适应边际来减少说话人信息。
- **RiemannSD-AAM**：将源和说话人嵌入投影到双曲空间，利用黎曼度量距离建模复杂分布，以更好解缠说话人特征并学习更具区分性的源特征。

# 实验结果
在MLAAD基准测试中，使用四种新提出的协议（针对源-说话人解缠场景）评估SDML框架。结果显示，RiemannSD-AAM在所有测试模型（如ECAPA-TDNN、ResNet34、AASIST、Mamba）中表现最佳，显著降低等错误率（EER）并提高AUC值，表明方法有效提高了源验证性能。

# 一句话评价
该研究首次结合切比雪夫多项式和黎曼度量学习，提出一个创新的说话人解缠框架，显著增强了深度伪造源验证的鲁棒性和准确性。

---

## 5. DiT-Flow: Speech Enhancement Robust to Multiple Distortions based on Flow Matching in Latent Space and Diffusion Transformers

**作者**: Tianyu Cao, Helin Wang, Ari Frummer, Yuval Sieradzki, Adi Arbel, Laureano Moro Velazquez, Jesus Villalba, Oren Gal, Thomas Thebaud, Najim Dehak
**链接**: [2603.21608](https://arxiv.org/abs/2603.21608)
**分类**: Speech Enhancement | **关键词**: Speech Enhancement, Generative Model, Flow Matching, Diffusion Transformers, Latent Space, Synthetic Data, LoRA, MoE

# 详细总结

## 核心痛点
- 现有语音增强模型在有限数据集上训练，评估条件狭窄，限制实际应用，尤其是在真实世界多变声学环境下。
- 合成数据集声学真实性不足，如使用简化房间脉冲响应，无法捕捉复杂声学条件，导致训练与部署条件不匹配。
- 扩散模型等生成方法计算密集、延迟高，不适合实时应用，如语音通信系统。
- 训练数据难以涵盖所有部署中可能遇到的失真类型，如噪声、混响和压缩伪影。

## 方法创新
- 提出DiT-Flow框架：基于流匹配（Flow Matching）的语音增强方法，构建在潜在扩散变换器（DiT）骨干上，在变分自编码器（VAEs）衍生的潜在特征上操作，降低计算成本。
- 引入StillSonicSet数据集：新的合成数据集，包含复杂房间几何、多样化表面材料和自然遮挡，提升声学真实性。
- 集成LoRA与MoE框架：实现参数高效训练，仅使用总参数的4.9%，动态激活不同LoRA专家，适应多种失真条件。
- 创新地结合流匹配与潜在空间操作，提高生成效率和鲁棒性。

## 实验结果
- 在StillSonicSet数据集上训练DiT-Flow，验证其在噪声、混响、压缩等多种失真下的鲁棒性。
- 实验表明，DiT-Flow consistently outperforms state-of-the-art generative SE models，在多种条件下表现优异。
- 在五个未见失真上实现更好性能，参数效率高，适合实际部署。

## 一句话评价
DiT-Flow通过流匹配、潜在空间技术和参数高效适应，为多失真语音增强提供了一个高效、鲁棒且可扩展的解决方案。

---

## 6. SqueezeComposer: Temporal Speed-up is A Simple Trick for Long-form Music Composing

**作者**: Jianyi Chen, Rongxiu Zhong, Shilei Zhang, Kun Qian, Jinglei Liu, Yike Guo, Wei Xue
**链接**: [2603.21073](https://arxiv.org/abs/2603.21073)
**分类**: Music Generation | **关键词**: long-form music generation, temporal speed-up, SqueezeComposer, diffusion models, audio acceleration

# 详细总结

## 核心痛点
长形式音乐生成面临两个主要挑战：1) 高计算和内存需求，因为音频表示序列长度与时间成正比，导致冗余和资源限制；2) 长期依赖建模困难，难以保持全局音乐连贯性和主题连续性。

## 方法创新
论文提出 SqueezeComposer，一个简单而强大的策略：通过时间加速音频（如 2×、4×、8×）来减少序列长度和计算需求。具体来说，先在加速域生成音乐（使用扩散模型在 Mel 谱图上操作），然后恢复原速以恢复完整时间结构。这种方法模型无关，遵循从抽象到详细内容的层次生成原则，并能直接应用于现有音乐生成模型。

## 实验结果
在以下两个任务上验证有效性：1) 长形式音乐生成（评估时间控制，包括续写、补全和从头生成）；2) 全歌伴唱生成（评估音轨控制）。实验结果表明，该方法实现了高效、可扩展和高质量的长形式音乐生成，音频样本在指定网站可获取。

## 一句话评价
SqueezeComposer 提供了一种创新且实用的策略，通过时间加速有效缓解了长形式音乐生成的资源瓶颈，同时保持音乐质量。

---

## 7. OmniCodec: Low Frame Rate Universal Audio Codec with Semantic-Acoustic Disentanglement

**作者**: Jingbin Hu, Haoyu Zhang, Dake Guo, Qirui Zhan, Wenhao Li, Huakang Chen, Guobin Ma, Hanke Xie, Chengyou Wang, Pengyuan Xie, Chuan Xie, Qiang Zhang, Lei Xie
**链接**: [2603.20638](https://arxiv.org/abs/2603.20638)
**分类**: Audio Codec for Audio Generation | **关键词**: Universal Audio Codec, Low Frame Rate, Semantic-Acoustic Disentanglement

### 核心痛点
大多数现有神经音频编解码器（如SoundStream、DAC、Encodec）专注于高保真重建，需要高帧率和比特率，忽略了跨多样音频域（语音、音乐、通用声音）的统一低帧率建模。此外，高重建质量不一定产生语义信息丰富的表示，限制了在下游基于大语言模型（LLM）的生成任务中的有效性。

### 方法创新
提出OmniCodec，一个为低帧率设计的通用神经音频编解码器。关键创新包括：
- **语义-声学解耦**：利用预训练理解模型Qwen3-Omni-AuT-Encoder的音频编码器作为语义分支输入，实现语义和声学表示的分离，提升语义信息建模能力。
- **分层多码本设计**：采用向量量化（VQ）和残差向量量化（RVQ）的分层结构，支持低帧率（12.5 Hz和6.25 Hz），适配LLM的令牌空间。
- **自引导策略**：引入自引导损失，引导解码器处理量化令牌和连续预量化潜在表示时产生相似输出，提高码本利用率和重建质量。
- **纯因果感受野**：模型设计支持流式处理和快速推理，适用于实时音频应用。

### 实验结果
在LibriSpeech（语音）、GTZAN（音乐）和AudioSet（通用声音）数据集上进行评估，使用指标如PESQ-WB、STOI、Mel距离等。OmniCodec在相同比特率下，相比基线模型如Mimi codec、UniCodec和AUV，实现了显著更优的重建质量，并提供了更语义信息丰富的表示，有利于下游音频生成任务。例如，OmniCodec-32L在4400 bps比特率下，在语音、音乐和通用声音域均表现出色。

### 一句话评价
OmniCodec是一个创新的低帧率通用音频编解码器，通过语义-声学解耦和自引导机制，在重建质量和语义表示上均超越现有方法，为基于LLM的音频生成提供了高效的音频标记器。

---

## 8. End-to-End Multi-Task Learning for Adjustable Joint Noise Reduction and Hearing Loss Compensation

**作者**: Philippe Gonzalez, Vera Margrethe Frederiksen, Torsten Dau, Tobias May
**链接**: [2603.20387](https://arxiv.org/abs/2603.20387)
**分类**: Audio Enhancement | **关键词**: Multi-task learning, Noise reduction, Hearing loss compensation

# 核心痛点
听力障碍患者在全球范围内面临社交、认知和生活质量下降的挑战，传统助听器方法独立优化噪声减少（NR）和听力损失补偿（HLC），导致在复杂声学环境中表现不佳。现有深度学习（DNN）方法需要训练额外的听觉模型仿真器，缺乏可微分模型，限制了端到端优化和个性化应用。

# 方法创新
提出端到端多任务学习框架，使用单个深度神经网络（DNN）预测两个时频掩码，分别对应 NR 和 HLC。集成固有可微分的听觉模型，允许通过指数调整掩码独立控制 NR 和 HLC 量，无需训练仿真器。听力图作为 DNN 输入，实现听者特异性个性化，无需为每个用户重新训练。

# 实验结果
方法能独立调整 NR 和 HLC，客观指标优于单一训练目标优化。在性能上超过分别训练 NR 和 HLC 的两个 DNN 级联，并与传统助听器处方（如 FIG6）竞争。这是首个使用听觉模型为广泛听者配置文件训练单个 DNN 进行联合 NR 和 HLC 的研究。

# 一句话评价
该研究创新地结合多任务学习和可微分听觉模型，为个性化、可调整的助听器信号处理提供了高效端到端解决方案。

---

## 9. TiCo: Time-Controllable Training for Spoken Dialogue Models

**作者**: Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu, Hung-yi Lee, James Glass
**链接**: [2603.22267](https://arxiv.org/abs/2603.22267)
**分类**: Spoken Dialogue Generation | **关键词**: TiCo, Spoken Dialogue Models, Time Control, Spoken Time Markers, Reinforcement Learning

## 核心痛点
现有 Spoken Dialogue Models (SDMs) 缺乏时间意识，难以遵循明确的时长指令（例如生成约15秒的响应），这限制了在语音助手等现实应用中的交互质量和实用性，因为控制响应时长对于提升用户体验至关重要。

## 方法创新
提出 TiCo，一个两阶段后训练框架：第一阶段通过自我生成与 Spoken Time Markers (STMs) 训练模型的时间意识，使模型能估计已用时长；第二阶段使用强化学习与可验证奖励来优化时长控制，使模型在生成过程中实时调整响应以满足目标时长，同时保持响应质量。

## 实验结果
通过 TiCo-Bench 评估，TiCo 显著提高了 SDMs 对时长约束的遵守率，实验结果表明响应质量得以保持，并且该方法能够泛化到训练中未见的时长范围。

## 一句话评价
TiCo 提供了一种简单高效的后训练方法，有效解决了 SDMs 中时间可控性的挑战，具有实际应用潜力。

---

## 10. Semi-Blind Channel Estimation and Hybrid Receiver Beamforming in the Tera-Hertz Multi-User Massive MIMO Uplink

**作者**: Abhisha Garg, Suraj Srivastava, Varsha Dubey, Aditya Jagannatham, Lajos Hanzo
**链接**: [2603.22258](https://arxiv.org/abs/2603.22258)
**分类**: Tera-Hertz Massive MIMO Systems | **关键词**: Tera-Hertz, Massive MIMO, Semi-Blind Channel Estimation, Hybrid Beamforming, Multi-User Uplink

# 核心痛点

THz 通信系统面临高路径损失、分子吸收和大气湍流等挑战，导致信道估计困难。传统训练-based 方法需要大量导频，降低频谱效率；盲估计方法计算复杂度高且收敛不稳定。

# 方法创新

- 提出多用户白化去相关半盲（MU-WD-SB）信道状态信息获取技术，结合导频向量和未知数据符号的二阶统计量。
- 推导约束 Cramér-Rao 下界（C-CRLB）以 bound 归一化均方误差（NMSE）性能。
- 设计基于多测量向量稀疏贝叶斯学习（MMV-SBL）的混合接收机组合框架，利用低分辨率模数转换器（ADCs）估计的 CSI。
- 提出基于 MMV-SBL 的最优混合组合器，直接减少多用户干扰。

# 实验结果

通过广泛模拟，使用高分辨率传输（HITRAN）数据库的实际 THz 信道，评估了所提 MU-WD-SB 方案在 NMSE、误码率（BER）和频谱效率（SE）方面的性能增益，优于传统训练-based 和其他半盲学习技术。

# 一句话评价

该论文创新性地将半盲学习应用于 THz 大规模 MIMO 系统，有效降低了训练开销并提高了信道估计准确性，为下一代无线通信提供了实用解决方案。

---

## 11. TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset and Preliminary Results with Scalable Data Mining In-the-Wild

**作者**: Kai-Wei Chang, Yi-Cheng Lin, Huang-Cheng Chou, Wenze Ren, Yu-Han Huang, Yun-Shao Tsai, Chien-Cheng Chen, Yu Tsao, Yuan-Fu Liao, Shrikanth Narayanan, James Glass, Hung-yi Lee
**链接**: [2603.21478](https://arxiv.org/abs/2603.21478)
**分类**: Spoken Language Understanding | **关键词**: spoken language understanding, low-resource language, intent recognition, Taiwanese Hokkien, dataset

**核心痛点**
低资源语言如台湾台语（Taiwanese Hokkien/Southern Min）在语音技术中代表性不足，尤其是在老年人中缺乏真实世界意图识别数据集。台语主要口语化，缺乏标准书写系统，导致可靠自动语音识别（ASR）系统不可用，限制了医疗保健和家庭助手等场景的实用口语语言理解（SLU）系统开发。

**方法创新**
引入了TaigiSpeech数据集，包含21位老年人（年龄54-78岁）的3,079条真实世界话语，涵盖8个意图类别（4个紧急意图和4个非紧急意图）。为解决标注数据稀缺，探索了两种可扩展的数据挖掘策略：1) 关键词匹配挖掘，利用中间语言（如中文）的副标题通过大语言模型伪标签；2) 音频-视觉挖掘，利用多模态线索最小化文本监督。这些方法支持低资源和无书写语言的数据集构建。

**实验结果**
评估了轻量级神经网络和自监督学习（SSL）语音模型等基线模型。实验结果显示，在挖掘数据上训练的模型在真实世界老年人录音上评估时性能显著下降，表明域不匹配，突出了现实部署的挑战。这强调了TaigiSpeech作为低资源SLU现实基准的必要性。

**一句话评价**
这项研究为低资源语言口语理解提供了宝贵的真实世界数据集和实用数据挖掘方法，同时揭示了现实世界部署中的域不匹配问题，促进了老年友好技术的开发。

---

## 12. HELIX: Scaling Raw Audio Understanding with Hybrid Mamba-Attention Beyond the Quadratic Limit

**作者**: Khushiyant, Param Thakkar
**链接**: [2603.21316](https://arxiv.org/abs/2603.21316)
**分类**: Audio Representation Learning | **关键词**: HELIX, Mamba, Attention, Hybrid Models, Raw Audio

## 核心痛点
音频表示学习通常孤立地评估设计选择（如输入前端、序列主干和序列长度），但这些轴是耦合的，导致结论不通用。纯注意力模型在长序列上面临二次方计算复杂度和内存限制，而压缩前端（如mel-spectrograms）会丢失相位和精细时间细节，限制了模型性能。

## 方法创新
引入HELIX控制实验框架，参数匹配在约8.3M参数，比较纯Mamba、纯注意力和一个最小混合模型（带单个注意力瓶颈）。混合模型结合原始波形前端、双向Mamba主干和单个全局注意力层，旨在隔离架构效应并提供全局交互能力。框架设计允许独立变化输入表示、主干家族和注意力比例，以研究它们之间的交互作用。

## 实验结果
在六个数据集上的实验显示：输入表示的偏好取决于主干架构；注意力在短、静止音频任务中可能损害性能，但在长序列（如5分钟、30,000令牌）上变得关键。具体地，在5分钟说话人识别任务中，纯注意力模型因内存溢出失败，而HELIX混合模型在纯Mamba基础上弥补了11.5点的性能差距。结果表明，设计选择应根据任务和序列长度动态调整。

## 一句话评价
HELIX提供了一个控制框架，揭示了音频表示学习中设计选择之间的耦合，并通过混合Mamba-Attention架构有效扩展到长序列任务，为未来音频模型优化提供了指导。

---

## 13. ALICE: A Multifaceted Evaluation Framework of Large Audio-Language Models' In-Context Learning Ability

**作者**: Yen-Ting Piao, Jay Chiehen Liao, Wei-Tang Chien, Toshiki Ogimoto, Shang-Tse Chen, Yun-Nung Chen, Chun-Yi Lee, Shao-Yuan Lo
**链接**: [2603.20433](https://arxiv.org/abs/2603.20433)
**分类**: Audio-Language Model Evaluation | **关键词**: Large Audio-Language Models, In-Context Learning, Evaluation Framework

## 核心痛点
Large Audio-Language Models (LALMs) 在指令跟随能力方面表现出下降，特别是在音频条件下。目前，LALMs 的上下文学习（ICL）能力在音频条件下尚未得到系统研究，存在显著的知识差距。

## 方法创新
提出 ALICE（Audio-Language In-Context learning Evaluation）框架，一个三阶段评估方法，逐步减少文本指导：Stage 1（明确约束）、Stage 2（隐含约束）和 Stage 3（仅音频）。该框架通过控制音频输入和演示输出，隔离文本线索的贡献，以评估 LALMs 能否从音频条件下的示例中推断任务目标和生成正确格式的响应。

## 实验结果
在六个 LALMs（包括 Qwen2-Audio、DeSTA2.5-Audio、BLSP-Emo、Qwen2.5-Omni、Phi-4-Multimodal 和 Gemini 2.5 Flash）上评估四个音频理解任务（ASR、SER、GR、MMAU）和两个输出约束类别（CEQ 和 CoT）。结果显示一致的对称性：上下文演示改善了格式遵从性（Format Compliance Rate），但未能改善甚至降低了核心任务性能（如 Word Error Rate 和准确性）。这表明 LALMs 能从演示中学习表面格式模式，但难以利用跨模态语义接地来可靠推断任务目标。

## 一句话评价
ALICE 提供了一个创新的系统框架，揭示了 LALMs 在跨模态上下文学习中的关键局限性，为未来模型改进和跨模态集成研究提供了重要见解。

---

## 14. Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education

**作者**: Abdul Aziz Snoubara, Baraa Al_Maradni, Haya Al_Naal, Malek Al_Madrmani, Roaa Jdini, Seedra Zarzour, Khloud Al Jallad
**链接**: [2603.20255](https://arxiv.org/abs/2603.20255)
**分类**: Speech Classification | **关键词**: speech classification, child speech classification, Arabic Speech classification, low-resource language, numbers speech classification, alphabets speech classification

### 核心痛点
儿童语音分类研究受限，尤其对于低资源语言如阿拉伯语，缺乏公开、大规模、多样化的数据集。现有模型基于成人语音，难以泛化到儿童语音，因儿童语音具有独特的声学和语言特征（如声调高、发音不一致），且阿拉伯语音素间相似度高，加剧分类难度。

### 方法创新
提出Abjad-Kids数据集，包含46,397个阿拉伯语儿童语音样本（来自3-12岁儿童，141个类别，覆盖字母、数字和颜色），所有样本在控制规格下录制（如2秒时长、16 kHz采样率）。设计分层音频分类方法，基于CNN-LSTM架构：采用两阶段策略，首先通过分组模型（静态基于语言学发音点分组或动态聚类分组）将相似类别分组，然后在每个组内使用专门分类器。此方法旨在减少类别混淆，应对高类内相似性和有限样本问题。

### 实验结果
实验评估表明，静态基于语言学分组方法性能优于动态聚类分组。CNN-LSTM模型结合数据增强（如合成数据）有效提升分类效果，但大部分实验出现过拟合挑战，可能由于样本数量有限，即使使用数据增强和模型正则化。结果突显了数据稀缺对模型泛化的影响。

### 一句话评价
该研究通过引入Abjad-Kids数据集和创新的分层分类方法，为阿拉伯语儿童语音分类领域提供了宝贵资源和技术框架，有助于推动低资源语言教育技术发展。

---

## 15. LL-SDR: Low-Latency Speech enhancement through Discrete Representations

**作者**: Jingyi Li, Luca Della Libera, Mirco Ravanelli, Cem Subakan
**链接**: [2603.20242](https://arxiv.org/abs/2603.20242)
**分类**: Speech Enhancement | **关键词**: speech enhancement, discrete representations, low-latency

# 核心痛点
- 现有语音增强方法常依赖连续表示，自回归架构（如 SELM、GenSE）虽性能优异，但延迟高，难以满足实时应用（如电信、助听器）的低延迟需求。
- 在非自回归框架中，连续表示可能未充分利用离散表示的潜力，导致性能受限。

# 方法创新
- 提出 LL-SDR 框架：一个基于令牌的非自回归语音增强模型，通过离散表示实现低延迟。
- 引入方差有序残差向量量化器（VO-RVQ）：通过三角形掩码结构解纠缠语音（高方差）和噪声（低方差）分布。
- 设计语义判别器：基于 HuBERT 的判别器用于对齐增强嵌入和语义嵌入，提升语义保真度。
- 整体架构轻量，结合重建损失、排序损失和对比损失优化。

# 实验结果
- 在 DNSMOS 指标上，LL-SDR 在混响和非混响噪声环境中优于连续基线（如 Conv-TasNet、FRCRN），匹配自回归方法（如 GenSE、LLaSE-G1）的性能。
- 计算效率：在 GPU 上实现最低实时因子（RTF），表明低延迟特性；在 CPU 上也表现高效。
- 定量和定性分析（如 t-SNE 可视化）证实 VO-RVQ 能有效分离语音和噪声。

# 一句话评价
LL-SDR 通过离散表示和解纠缠技术，提供了一个高效、低延迟的语音增强解决方案，在保持性能的同时显著降低延迟。

---

