# Arxiv Daily Deep Report - 2026-08-25

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 6
---

## 1. TurboBias 2.0: Streaming Context-Biasing for Production-Efficient ASR Systems

**作者**: Vladimir Bataev, Lilit Grigoryan, Andrei Andrusenko, Nikolay Karpov, Vitaly Lavrukhin, Boris Ginsburg
**链接**: [2608.21343](https://arxiv.org/abs/2608.21343)
**分类**: Speech Recognition | **关键词**: Automatic Speech Recognition (ASR), Context Biasing, Phrase Boosting, Transducers, Streaming Inference

### 核心痛点
现代生产 ASR 系统需要准确识别用户自定义短语（上下文词组），但现有方法在流式推理、高效批处理、个性化上下文列表和低开销方面存在不足。此外，用户提供的短语与模型输出在大小写上可能不一致，导致匹配失败。

### 方法创新
TurboBias 2.0 提出了面向生产的 Transducer ASR 上下文偏置框架，主要包括：
1. **大小写不敏感的字词提升图**：通过变体 BPE 表示和字符级合并弧，在不增加短语变体的情况下实现大小写不敏感的匹配，并利用累计势能函数分配分数，保证不同分割获得相同总提升。
2. **每流上下文偏置**：在 GPU 批处理中，每个流使用独立的偏置图，通过合并多模型存储和偏移量管理，实现动态添加/移除短语列表，避免跨流干扰。
3. **流式解码支持**：支持流式贪心搜索和 beam search，并保持低运行时开销。

### 实验结果
在 Contextual Earnings-22 和内部医学领域测试集上，TurboBias 2.0 相比基线提升了上下文短语识别质量，同时保持了低延迟和高吞吐。实验分析了大小写不敏感图与大小写敏感/短语展开方案的效果差异，以及离线/流式解码模式、beam 大小、F-score 与延迟的折中。

### 一句话评价
TurboBias 2.0 是针对流式 Transducer ASR 的高效、可扩展上下文偏置方案，兼顾了大小写鲁棒性和个性化批处理需求，适合生产部署。

---

## 2. SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhancement using Slimmable Networks

**作者**: Nagashree K. S. Rao, Shrishti Saha Shetu, Mohamed Elminshawi, Emanuël A. P. Habets, Andreas Brendel
**链接**: [2608.21188](https://arxiv.org/abs/2608.21188)
**分类**: Speech Enhancement | **关键词**: Diffusion Models, Speech Enhancement, Slimmable Neural Networks, Efficient Inference, Computational Complexity Reduction

## 核心痛点
扩散模型在语音增强中性能优异，但需要多个反向扩散步骤反复评估大型神经网络，计算复杂度高，难以用于实时应用。

## 方法创新
提出 SlimDiffuSE，一种基于 SGMSE+ 的可瘦身扩散模型。通过利用可瘦身神经网络（SNN），在推理过程中自适应调整网络宽度（利用因子 u），按扩散步骤动态分配计算资源。训练时采用多宽度优化策略，推理时通过贪心搜索优化每个步骤的宽度调度。在保持参数数量的同时，显著降低整体计算成本。

## 实验结果
在 DNS 数据集上，预定义的混合复杂度配置显示，反向扩散早期（t 接近1）需要高容量模型，而后期（t 接近0）低容量模型即可满足需求。SlimDiffuSE 通过可瘦身网络实现类似配置，性能与完整模型相当，计算复杂度可降低高达 87.5%。

## 一句话评价
一种高效扩散语音增强方法，通过按步骤动态分配网络宽度，在不牺牲性能的前提下大幅降低计算负担。

---

## 3. μNet: Ultra-Low-Memory and Low-Complexity Speech Enhancement for Embedded Digital Signal Processors

**作者**: Shrishti Saha Shetu, Jose Miguel Martinez Aponte, Nagashree K. S. Rao, Sharvin Vittappan, Oliver Thiergart, Emanuël A. P. Habets
**链接**: [2608.21155](https://arxiv.org/abs/2608.21155)
**分类**: Speech Enhancement | **关键词**: speech enhancement, low-memory, low-complexity, embedded DSP, integer quantization

# 核心痛点
- 嵌入式DSP上的语音增强受限于内存、计算复杂度、延迟和整数运算支持。
- 现有DNN方法难以同时满足这些约束，多数SOTA模型延迟高（10-40ms），不适合助听器等场景。
- 现有低延迟技术未充分联合优化延迟、内存和定点(int8)操作支持。

# 方法创新
- 提出μNet，一种超低内存（90KB）、低复杂度（28MMACs）和低延迟（4ms）的端到端DNN。
- 基于ULCNet改进，采用两阶段架构：第一阶段估计幅度掩码，第二阶段估计复比掩码。
- 结合C-SubFR和C-SamFR特征重定向，捕获局部和全局频谱依赖。
- 使用标准卷积而非深度可分离卷积，以适配嵌入式硬件和量化。
- 共享子带GRU和共享线性投影，显著降低参数。
- 支持全int8量化，兼容Cadence Tensilica HiFi 4/5等DSP。
- 提供可配置噪声衰减控制(NAL)，权衡噪声抑制与语音质量。

# 实验结果
- 在DNS挑战数据集上，μNet-MSE仅46K参数、28MMACs、90KB内存，性能与RNNoise、GTCRN相当。
- μNet-MSE在噪声抑制(BAK 4.03)上优于基线，PESQ 1.90、SI-SDR 13.24dB。
- 与自注意力(μNet V2)和门控卷积(μNet V3)变体相比，共享GRU在更低复杂度下表现竞争。
- 消融实验显示功率律因子和NAL设置对性能有影响，听感测试确认了主观质量。

# 一句话评价
μNet为嵌入式DSP提供了一种超低内存、低复杂度、低延迟且可量化部署的实用语音增强方案，在资源受限场景下具有很强应用价值。

---

## 4. Training DeepFilterNet with Accurate Room Acoustic Simulations Improves Single-Channel Speech Enhancement

**作者**: Alessia Milo, Georg Götz, Steinar Guðjónsson, Daniel Gert Nielsen, Jesper Pedersen, Finnur Pind
**链接**: [2608.20971](https://arxiv.org/abs/2608.20971)
**分类**: Speech Enhancement | **关键词**: Speech enhancement, Room impulse response (RIR) simulation, DeepFilterNet, Reverberation modeling, Automatic speech recognition (ASR)

# 核心痛点
传统基于图像源法（ISM）的合成RIR数据集无法充分捕捉真实声学条件，导致语音增强模型在真实环境中的泛化能力受限。

# 方法创新
本文比较了ISM与高保真混合仿真的RIR数据集对DeepFilterNet3训练的影响。混合仿真结合波法和几何声学，在低频准确建模模态、衍射等，高频用GA，提高RIR的真实感。

# 实验结果
训练于混合数据集（Hybrid）的DeepFilterNet3在所有配置下均获得客观指标提升（PESQ +0.166, SI-SDRi +0.110, STOI +0.013, SRMR +0.270），并在下游ASR上大幅降低词错误率（WER）。

# 一句话评价
研究表明提高合成RIR的整体真实感能有效改善语音增强模型在未知真实环境的泛化性能。

---

## 5. A Regularized Block Diagonal RLS Algorithm for Acoustic Echo Cancellation

**作者**: Ruibin Hou, Chenggang Zhang, Yufeng Diao
**链接**: [2608.20693](https://arxiv.org/abs/2608.20693)
**分类**: Acoustic Echo Cancellation | **关键词**: Acoustic echo cancellation, recursive least squares, block-diagonal approximation, regularization

## 核心痛点
- 传统RLS算法计算复杂度高（O(N^2)），且数值稳定性差，在长滤波器（如AEC中N=512~2048）下难以实时部署。
- LMS收敛慢，FRLS数值不稳定，RLS-DCD虽然有低复杂度但存在O(N^2)数据复制开销，不适合通用处理器。

## 方法创新
- 提出正则化块对角RLS（RBD-RLS）算法，将N阶自相关矩阵近似为块对角结构，分解为M个独立子块并行更新，复杂度降为O(NL)。
- 引入Tikhonov正则化（对角加载）确保各子块矩阵正定性，避免初期数值发散。
- 通过块处理策略，将滤波器分割为子向量，并推导出分块更新的递推公式。

## 实验结果（根据摘要及片段）
- 实验表明RBD-RLS在保持良好收敛性能的同时，显著降低计算复杂度。
- 在真实场景中表现出较强的鲁棒性。
- 参数L调节复杂度与收敛性能的折中，L越大越接近RLS但复杂度增加。

## 一句话评价
RBD-RLS通过块对角近似和正则化，在计算复杂度、收敛速度和数值稳定性之间取得了有效平衡，适合用于声学回声消除等长滤波器场景。

---

## 6. Building and Evaluating a Synthetic Bengali Speech Resource for Telecom Customer Care

**作者**: Kawshik Kumar Paul, Md. Nafiul Alam Fuji
**链接**: [2608.20346](https://arxiv.org/abs/2608.20346)
**分类**: Text-to-Speech | **关键词**: Synthetic Speech, Bengali, Telecom Customer Care, Text-to-Speech, WER

## 核心痛点
现有语音系统在特定领域（如电信客户服务）需要领域特定的语言覆盖。虽然存在如Common Voice等众包语音资源，但广泛领域且多为人类录音，缺乏针对孟加拉语电信客户服务的合成语音数据。

## 方法创新
论文构建了一个10,000音频-文本对的合成孟加拉语语音数据集，总时长约26.82小时，采样率24kHz。使用OmniVoice TTS在语音克隆模式下生成，参考真实女性录音和转录。数据划分为训练/验证/测试（9000/500/500）。同时，提供原始文本和归一化转录字段。评估使用基于Whisper的ASR模型（从Tugstugi Whisper微调）进行自动可懂度检查，并辅以人工听力检查。

## 实验结果
平均WER为2.54%，平均CER为0.59%，中位数WER和CER均为0.00%，表明合成语音与文本一致性较强。

## 一句话评价
该论文为孟加拉语电信客户服务领域提供了首个公开的合成语音数据集，并通过自动和人工评估验证了其质量，对领域相关ASR/TTS研究有重要价值。

---

