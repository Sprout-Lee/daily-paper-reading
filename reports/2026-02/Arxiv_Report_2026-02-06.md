# Arxiv Daily Deep Report - 2026-02-06

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 6
---

## 1. Zero-Shot TTS With Enhanced Audio Prompts: Bsc Submission For The 2026 Wildspoof Challenge TTS Track

**作者**: Jose Giraldo, Alex Peiró-Lilja, Rodolfo Zevallos, Cristina España-Bonet
**链接**: [2602.05770](https://arxiv.org/abs/2602.05770)
**分类**: Text-to-Speech | **关键词**: zero-shot TTS, audio enhancement, non-autoregressive models, wildspoof challenge, speech synthesis

## 核心痛点
论文针对在野外（in-the-wild）语音数据上训练文本转语音（TTS）系统的挑战，包括环境噪声和声学条件导致的转录错误、以及自发语音中韵律和说话风格的多样性（如犹豫、填充词和可变节奏）使时长建模更加困难。

## 方法创新
1. **语音增强**：使用Sidon模型进行多阶段增强管道，显著优于标准Demucs，提高信号质量。
2. **非自回归架构**：采用StyleTTS2和F5-TTS模型，结合灵活的时长建模，以改善韵律自然度。
3. **微调策略**：在增强后的TITW-Easy数据集上微调预训练模型，而非从头训练，以提升鲁棒性。
4. **推理参数分析**：系统分析参考提示（音频提示）的质量和长度对零样本合成性能的影响，优化音频质量和可懂度。

## 实验结果
- **音频质量**：使用增强音频提示后，F5-TTS和StyleTTS2在UTMOS和DNSMOS指标上均有提升，最高达到4.21 UTMOS和3.47 DNSMOS。
- **可懂度**：增强参考音频降低了词错误率（WER），尤其在StyleTTS2中效果更明显。
- **说话人相似性**：提示长度与说话人相似性直接相关，长提示（平均7.7秒）优于短提示（平均5.5秒），但增强可能轻微降低相似性分数。
- **模型比较**：F5-TTS在可懂度和说话人相似性方面表现更稳定，而StyleTTS2在音频质量提升上更显著。从头训练的小型F5-TTS变体性能较差，确认了从大规模语音预训练中迁移学习的价值。
- **最终选择**：为WildSpoof挑战赛提交了使用增强参考提示的F5-TTS样本，因其在可懂度、音频质量和说话人相似性方面综合表现最佳。

## 一句话评价
该研究通过结合语音增强、非自回归架构和系统提示分析，有效提升了零样本TTS在野外语音数据上的性能，为现实语音生成提供了实用解决方案。

---

## 2. Wave-Trainer-Fit: Neural Vocoder with Trainable Prior and Fixed-Point Iteration towards High-Quality Speech Generation from SSL features

**作者**: Hien Ohnaka, Yuma Shirahata, Masaya Kawamura
**链接**: [2602.05443](https://arxiv.org/abs/2602.05443)
**分类**: Speech Synthesis | **关键词**: Neural Vocoder, Self-Supervised Learning, Variational Autoencoder, Speech Synthesis, Waveform Generation

## 核心痛点
传统WaveFit声码器在使用自监督学习（SSL）特征时面临两个主要问题：1）无法利用信号处理知识进行手工噪声采样，只能从高斯噪声开始推理；2）无法利用梅尔频谱图的能量信息进行增益调整，需要模型隐式学习能量预测。

## 方法创新
WaveTrainerFit在WaveFit基础上引入两个关键改进：
1. **可训练先验**：通过变分自编码器（VAE）学习目标语音的先验分布，使推理可以从接近目标语音的噪声开始，而非高斯噪声
2. **参考感知增益调整**：对可训练先验施加约束以匹配语音能量，使声码器无需隐式学习能量预测任务

## 实验结果
1. **质量提升**：相比WaveFit，WaveTrainerFit能以更少的推理步骤生成更自然的波形
2. **说话人相似度**：主观评估显示在说话人相似度方面优于基线方法
3. **鲁棒性**：对SSL特征提取深度具有鲁棒性，即使深层SSL特征（包含有限声学信息）也能生成自然波形
4. **效率**：减少了波形建模的复杂性，实现高质量波形生成

## 一句话评价
WaveTrainerFit通过引入可训练先验和参考感知增益调整，有效解决了SSL特征声码化中的噪声采样和能量预测问题，在保持高质量输出的同时显著提升了推理效率。

---

## 3. Exterior sound field estimation based on physics-constrained kernel

**作者**: Juliano G. C. Ribeiro, Ryo Matsuda, Jorge Trevino
**链接**: [2602.05236](https://arxiv.org/abs/2602.05236)
**分类**: Acoustic Signal Processing | **关键词**: Physics-informed machine learning, Sound field interpolation, Gaussian process regression, Exterior sound field problem

## 核心痛点
外部声场插值是一个具有挑战性的问题，传统方法通常需要特定的麦克风阵列配置和先验的源条件知识。现有方法如球面波函数展开（SWF）对正则化和麦克风分布敏感，而点神经元网络（PNN）等数据驱动方法在训练时可能因声压在源位置发散而困难。

## 方法创新
本文提出了一种基于高斯过程回归（GPR）的插值方法，使用具有可训练内积公式的点源再生核来拟合外部声场。该方法的核心创新包括：
1. **物理约束核设计**：基于非齐次亥姆霍兹方程的外部波函数解定义再生核希尔伯特空间（RKHS），确保满足物理约束。
2. **参数化加权内积**：引入径向权重函数（如指数衰减形式），自动衰减高阶谐波分量，参数α和β可从数据中优化。
3. **灵活性与通用性**：不限制麦克风分布，允许任意麦克风阵列配置，通过核岭回归（KRR）进行系数估计。

## 实验结果
在数值模拟中，将所提方法（Proposed）与球面波函数展开（SWF）和点神经元网络（PNN）进行比较：
- **性能指标**：在100 Hz至2.5 kHz频率范围内，所提方法平均降低插值误差约2 dB（归一化均方误差，NMSE）。
- **阵列鲁棒性**：在球形t-design阵列和随机分布阵列上均表现一致，优于对比方法。
- **重建质量**：在目标区域内更一致地重建真实声场，归一化平方误差（NSE）分布更优。

## 一句话评价
该研究通过物理约束核与数据驱动优化相结合，为外部声场插值提供了一种灵活且高性能的解决方案，显著提升了插值精度和阵列鲁棒性。

---

## 4. ARCHI-TTS: A flow-matching-based Text-to-Speech Model with Self-supervised Semantic Aligner and Accelerated Inference

**作者**: Chunyat Wu, Jiajun Deng, Zhengxi Liu, Zheqi Dai, Haolin He, Qiuqiang Kong
**链接**: [2602.05207](https://arxiv.org/abs/2602.05207)
**分类**: Text-to-Speech | **关键词**: flow matching, semantic aligner, non-autoregressive TTS, accelerated inference, zero-shot synthesis

## 核心痛点
1. **文本-语音对齐困难**：现有非自回归TTS模型在文本与音频的时序和语义对齐方面存在挑战，影响合成质量。
2. **推理计算成本高**：基于扩散的迭代去噪过程需要大量计算，导致推理效率低下。

## 方法创新
1. **自监督语义对齐器**：采用Transformer架构，通过掩码序列和文本特征交互，动态生成与语音长度匹配的语义表示，无需显式时长预测。
2. **加速推理策略**：分离的条件编码器-速度解码器架构，允许在去噪步骤间复用编码器特征，显著减少计算量。
3. **辅助CTC损失**：在条件编码器上应用CTC损失，增强语义理解和对齐。
4. **压缩语音潜在表示**：使用VAE将音频压缩为低令牌率（12.5Hz）潜在表示，替代高冗余的梅尔频谱。

## 实验结果
1. **性能指标**：在LibriSpeech-PC test-clean上WER为1.98%，在SeedTTS test-en/test-zh上分别为1.47%/1.42%。
2. **效率优势**：训练仅需8块RTX5090 GPU运行4天，数据量远少于典型系统，支持训练免费推理加速。
3. **主观质量**：在自然度、说话人相似度和质量方面的MOS评分与工业级TTS系统竞争。

## 一句话评价
ARCHI-TTS通过创新的对齐器和高效推理设计，在保持高质量零样本语音合成的同时，显著提升了计算效率，为实用化部署提供了新思路。

---

## 5. HyperPotter: Spell the Charm of High-Order Interactions in Audio Deepfake Detection

**作者**: Qing Wen, Haohao Li, Zhongjie Ba, Peng Cheng, Miao He, Li Lu, Kui Ren
**链接**: [2602.05670](https://arxiv.org/abs/2602.05670)
**分类**: Audio Deepfake Detection | **关键词**: Hypergraph, High-Order Interactions, Audio Deepfake Detection

## 核心痛点
音频深度伪造检测（ADD）现有方法主要依赖局部或成对特征交互，忽略了高阶交互（HOIs），导致难以捕捉合成音频中跨多个声学维度的协同伪影，限制了检测的泛化能力。

## 方法创新
提出HyperPotter，一种基于超图的框架，通过聚类超边和类感知原型初始化，显式建模高阶协同交互。关键组件包括：关系伪影放大模块和原型导向的超边初始化机制，以增强信息性协同伪影并高效构建关系。

## 实验结果
在11个数据集上平均相对增益22.15%，在4个跨域数据集上超越最先进方法13.96%，展示了在多样化攻击和说话者条件下的优越泛化性能。

## 一句话评价
该研究首次从信息论角度探讨音频深度伪造检测中的高阶效应，通过超图建模协同依赖，为提升检测泛化性提供了有效路径。

---

## 6. Phase-Only Positioning in Distributed MIMO Under Phase Impairments: AP Selection Using Deep Learning

**作者**: Fatih Ayten, Musa Furkan Keskin, Akshay Jain, Mehmet C. Ilter, Ossi Kaltiokallio, Jukka Talvitie, Elena Simona Lohan, Mikko Valkama
**链接**: [2602.05034](https://arxiv.org/abs/2602.05034)
**分类**: Wireless Positioning, Distributed MIMO, Deep Learning in Communications | **关键词**: Carrier phase positioning, Distributed MIMO, Deep learning, AP selection, Phase synchronization errors

## 核心痛点

论文针对分布式多输入多输出（D-MIMO）网络中的载波相位定位（CPP）问题，指出现有研究对相位同步误差的影响探索不足。这些误差会显著降低定位精度，而实际应用中还需满足低延迟要求，因此需要降低模型复杂度。

## 方法创新

1. **超椭圆交点方法**：在存在相位同步误差的情况下，通过训练反映此类损伤的数据，实现高精度定位。
2. **基于深度学习的AP选择框架**：提出一种深度学习（DL）方法，用于选择分布式天线点（AP），以在相位同步误差下确保高精度定位。该方法结合测量特征（如差分相位测量和信噪比）和几何特征（如AP间距离和角度），使用多层感知机（MLP）神经网络预测每个模糊度对的定位误差，从而选择最优AP对。
3. **系统架构**：引入分布式位置管理功能（DLMF），将部分定位任务移至用户设备（UE）附近，减少延迟并提高精度。

## 实验结果

1. **定位精度提升**：在模拟的D-MIMO网络拓扑中（9个AP，100平方米区域），与现有方法相比，提出的框架提高了定位精度。
2. **推理复杂度降低**：通过仅估计两个模糊度（而非全部），并结合AP选择模型，整体推理复杂度降低了约19.7%（从约1.262×10^6 FLOPs降至约1.014×10^6 FLOPs）。
3. **训练细节**：差分模糊度估计器使用70万个训练样本，AP选择网络使用20万个训练样本，均能有效处理相位扰动。

## 一句话评价

该论文通过深度学习优化AP选择，有效解决了D-MIMO中相位同步误差导致的定位精度下降问题，同时降低了计算复杂度，为6G部署提供了实用解决方案。

---

