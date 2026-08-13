# Arxiv Daily Deep Report - 2026-02-12

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 11
---

## 1. Self-Supervised Learning for Speaker Recognition: A study and review

**作者**: Theo Lepage, Reda Dehak
**链接**: [2602.10829](https://arxiv.org/abs/2602.10829)
**分类**: Speaker Recognition | **关键词**: Self-Supervised Learning, Speaker Recognition, Speaker Representations, Speech Processing

# 核心痛点
监督学习的深度模型在说话人识别中严重依赖大量人类标注数据，导致成本高昂、难以扩展，且在未见条件下泛化能力差。

# 方法创新
论文将自监督学习（SSL）实例不变性框架（如SimCLR、MoCo、DINO）应用于说话人识别，系统研究了SSL框架的超参数影响、组件角色（如数据增强、投影器、正采样），并比较了单阶段和多阶段SSL方法。

# 实验结果
在一致的实验设置下，DINO在下游任务中表现最佳，能有效建模说话人内部变异性，但对超参数和训练条件高度敏感；SimCLR和MoCo提供鲁棒替代，有效捕获说话人间变异性且不易崩溃。

# 一句话评价
这篇论文全面回顾了自监督学习在说话人识别中的应用，指出了当前挑战和未来研究方向。

---

## 2. RE-LLM: Refining Empathetic Speech-LLM Responses by Integrating Emotion Nuance

**作者**: Jing-Han Chen, Bo-Hao Su, Ya-Tse Wu, Chi-Chun Lee
**链接**: [2602.10716](https://arxiv.org/abs/2602.10716)
**分类**: Speech-LLM | **关键词**: speech LLM, empathetic AI, emotion nuance, dimensional emotion embeddings, auxiliary learning

# 论文总结：RE-LLM

## 核心痛点
现有同理心语言模型（LLMs）主要依赖文本输入，但文本在捕捉语音中的情感细微差别方面有限，导致情感探索能力不足，难以实现深度的人类-AI交互同理心。现有方法如BLSP-Emo虽然整合了语音，但仍缺乏对语音信号中情感细微变化的系统性建模，影响了同理心响应的质量。

## 方法创新
论文提出RE-LLM（Refining Empathetic Speech-LLM），通过集成维度情感嵌入和辅助学习来增强语音-LLMs。具体创新包括：
- **情感细微模块**：使用预训练的wav2vec 2.0模型提取维度情感嵌入（如效价、唤醒、优势），并将其与语音编码器输出结合，提供更丰富的情感信息。
- **多视角辅助任务**：在训练阶段引入分类（四类主要情感）和回归（三维情感属性）的辅助任务，以帮助模型更好地理解情感细微差别。
- **训练策略**：采用预处理生成预期响应和期望行为对齐的两步训练过程，优化KL散度损失，并结合交叉熵和均方误差损失进行整体训练。

## 实验结果
在三个数据集上（IEMOCAP、ESD、MSP-PODCAST）进行了评估：
- **同理心指标**：RE-LLM在情感反应分数上相对提升，例如在ESD上比文本-LLM基线提高14.79%，比语音-LLM基线提高6.76%。探索分数提升更显著，如在ESD上相对提升139.28%和9.83%。
- **语音情感识别**：无权重准确率在IEMOCAP上提高5.4%，在ESD上提高2.3%，在MSP-PODCAST上提高6.9%。
- 所有改进均通过Wilcoxon符号秩检验验证为统计显著，表明模型在同理心响应生成和情感理解方面有实质性进步。

## 一句话评价
RE-LLM通过融合语音情感细微差别和引入辅助学习任务，有效提升了语音-LLMs的同理心响应能力，为未来同理心AI交互提供了有前景的方法。

---

## 3. From Diet to Free Lunch: Estimating Auxiliary Signal Properties using Dynamic Pruning Masks in Speech Enhancement Networks

**作者**: Riccardo Miccini, Clément Laroche, Tobias Piechowiak, Xenofon Fafoutis, Luca Pezzarossa
**链接**: [2602.10666](https://arxiv.org/abs/2602.10666)
**分类**: Speech Enhancement | **关键词**: Speech Enhancement, Dynamic Pruning, Auxiliary Signal Estimation

### 核心痛点
语音增强（SE）系统通常需要辅助模块（如语音活动检测、信噪比估计、声学场景分类）以实现稳健的上下文感知行为，但这些模块的计算成本高，部署在边缘设备上不切实际，而云端推理会引入延迟并损害隐私。

### 方法创新
本研究提出利用动态通道剪枝（DynCP）模型中的剪枝掩码作为特征，通过简单的线性/逻辑回归模型预测辅助信号属性，如语音活动检测、噪声分类、F0估计等，避免了部署额外模型的计算开销。该方法利用了二进制掩码，使预测过程简化为加权和，计算开销可忽略。

### 实验结果
实验结果显示，在语音活动检测上达到93%准确率，噪声分类84%，F0估计R2为0.86。性能评估覆盖多个分类、回归和说话人验证任务，证明了该方法的有效性。

### 一句话评价
该工作创新地将动态剪枝技术应用于辅助任务估计，为边缘设备上的高效语音增强和信号属性提取提供了新思路。

---

## 4. AudioRAG: A Challenging Benchmark for Audio Reasoning and Information Retrieval

**作者**: Jingru Lin, Chen Zhang, Tianrui Wang, Haizhou Li
**链接**: [2602.10656](https://arxiv.org/abs/2602.10656)
**分类**: Audio Reasoning | **关键词**: Audio Reasoning, Information Retrieval

# 核心痛点
现有大型音频-语言模型（LALMs）的基准（如SAKURA和MMAR）主要评估模型基于内部知识的推理能力，忽视了现实世界场景中需要外部信息检索的情况。这导致模型在处理超出训练数据的问题时，容易产生幻觉，影响事实准确性。

# 方法创新
论文提出AudioRAG基准，首次系统评估音频推理与信息检索的结合能力。方法包括：1) 基于开源数据集和在线视频，使用LLM（如GPT-4o）生成和手动收集多跳问题-答案对；2) 设计代理管道，基于WebThinker增强音频处理工具和搜索工具，支持自主推理和外部知识检索。

# 实验结果
评估多个SOTA LALMs（如Qwen2.5-Omni、Audio Flamingo 3），结果显示准确率较低（如Qwen3-Omni为37.0%），证实模型难以处理音频推理和信息检索任务。代理管道（如Qwen3-Omni + Qwen3-8B）将准确率提升至46.2%，相对改进达24.9%，提供了强基线。

# 一句话评价
AudioRAG是一个创新性基准，有效填补了音频推理与信息检索结合的空白，为未来多模态AI研究提供了重要工具和方向。

---

## 5. SCRAPL: Scattering Transform with Random Paths for Machine Learning

**作者**: Christopher Mitcheltree, Vincent Lostanlen, Emmanouil Benetos, Mathieu Lagrange
**链接**: [2602.11145](https://arxiv.org/abs/2602.11145)
**分类**: Audio Processing and Differentiable Signal Processing | **关键词**: Scattering Transform, Random Paths, Stochastic Optimization, JTFS, DDSP

## 核心痛点
散射变换（Scattering Transform）在作为可微分损失函数时，由于路径众多，计算成本高且内存消耗大，严重限制了其在神经网络训练中的应用，特别是在大规模梯度下降中。这使得在音频、语音和计算机视觉领域的感知质量评估任务中，难以高效使用散射变换进行优化。

## 方法创新
论文提出SCRAPL（Scattering Transform with Random Paths for Machine Learning），一种随机优化方案，通过以下创新点提高效率：
- **随机路径采样**：均匀采样散射变换的路径来近似梯度，实现计算加速。
- **P-Adam（Path-wise Adaptive Moment Estimation）**：扩展Adam优化器，处理路径非独立同分布问题，通过路径自适应的矩估计平滑梯度。
- **P-SAGA（Path-wise Stochastic Average Gradient with Acceleration）**：基于SAGA算法的路径版本，维护路径梯度记忆以加速收敛。
- **θ-重要性采样**：初始化启发式方法，根据梯度变化率采样路径，提升优化性能。
这些方法共同减少散射变换的计算负担，使其适用于大规模可微分数字信号处理（DDSP）。

## 实验结果
在无监督声音匹配任务中，应用SCRAPL于粒度合成器和Roland TR-808鼓机，结果表明：
- 相比多尺度谱损失（MSS），SCRAPL在准确性上更优（例如，在感知质量评估中），计算成本略高但可接受。
- 相比完整联合时频散射变换（JTFS），SCRAPL在准确性上接近（在因子2内），但计算成本显著降低（在因子2内），内存效率更高，适合大规模部署。
- 实验通过平均合成器参数误差和计算成本评估，显示SCRAPL在帕累托前沿上取得平衡，优于其他基线方法。

## 一句话评价
SCRAPL是一种高效的随机优化框架，通过智能路径采样和优化技术，有效解决散射变换的计算瓶颈，在保持高性能的同时推动可微分信号处理和音频机器学习的发展。

---

## 6. Simultaneous Speech-to-Speech Translation Without Aligned Data

**作者**: Tom Labiausse, Romain Fabre, Yannick Estève, Alexandre Défossez, Neil Zeghidour
**链接**: [2602.11072](https://arxiv.org/abs/2602.11072)
**分类**: Simultaneous Speech-to-Speech Translation | **关键词**: Simultaneous Speech Translation, Speech-to-Speech Translation, Reinforcement Learning, GRPO, Sentence-level Alignment, Multistream Architecture

## 核心痛点
传统同时语音翻译（Simultaneous Speech-to-Speech Translation）方法依赖于单词级对齐的监督数据，但这些数据难以大规模收集，且通常基于语言特定的启发式方法进行合成对齐，导致效果不佳和流程复杂。

## 方法创新
论文提出Hibiki-Zero系统，创新点在于完全无需单词级对齐数据。首先使用句子级对齐数据训练基础模型，然后通过强化学习（RL）策略，具体采用GRPO（Group Relative Policy Optimization）优化延迟，同时保持翻译质量。基于多流架构（multistream architecture），模型同步处理源语音并生成目标语音和文本，奖励系统仅基于BLEU分数，简化了训练。

## 实验结果
在五个多语言到英语（X-to-English）任务中，Hibiki-Zero在翻译准确性、延迟、语音身份保留和自然度方面实现了最先进（state-of-the-art）性能。此外，模型能够以少于1000小时的语音数据适应新输入语言。作者发布了模型权重、推理代码和一个45小时的多语言基准数据集用于评估。

## 一句话评价
该方法通过消除对齐数据需求，显著简化了训练流程，提高了多语言可扩展性和实用性，为同时语音翻译领域带来了重要突破。

---

## 7. MOSS-Audio-Tokenizer: Scaling Audio Tokenizers for Future Audio Foundation Models

**作者**: Yitian Gong, Kuangwei Chen, Zhaoye Fei, Xiaogui Yang, Ke Chen, Yang Wang, Kexin Huang, Mingshu Chen, Ruixiao Li, Qingyuan Cheng, Shimin Li, Xipeng Qiu
**链接**: [2602.10934](https://arxiv.org/abs/2602.10934)
**分类**: Audio Tokenization | **关键词**: Audio Tokenizer, Transformer, End-to-End Learning

## 核心痛点
现有离散音频tokenizer方法通常依赖预训练编码器、语义蒸馏或异构CNN架构，这些设计引入了固定的归纳偏差，限制了重构保真度并阻碍了有效扩展。

## 方法创新
提出CAT（Causal Audio Tokenizer with Transformer），一个纯Transformer架构，从零开始联合优化编码器、量化器和解码器，实现高保真重构。基于CAT，开发了MOSS-Audio-Tokenizer，一个1.6亿参数的大规模音频tokenizer，在300万小时多样化音频数据上预训练，支持可变比特率（0.125 kbps 到 4 kbps）、低帧率（12.5 Hz）和流式处理。利用CAT的离散令牌，开发了首个纯自回归TTS模型，并提出了Progressive Sequence Dropout训练策略。

## 实验结果
MOSS-Audio-Tokenizer在语音、声音和音乐上，在各种比特率下一致优于现有编解码器，实现高保真重构。此外，它支持竞争性的自动语音识别（ASR）性能，无需辅助编码器，并显示出随着模型规模和计算预算增加而持续改进的重构质量。

## 一句话评价
CAT架构作为一个统一、可扩展的接口，为未来音频基础模型的音频压缩、理解和生成奠定了基础。

---

## 8. AudioRouter: Data Efficient Audio Understanding via RL based Dual Reasoning

**作者**: Liyang Chen, Hongkai Chen, Yujun Cai, Sifan Li, Qingwen Ye, Yiwei Wang
**链接**: [2602.10439](https://arxiv.org/abs/2602.10439)
**分类**: Audio Understanding | **关键词**: Large Audio Language Models, Reinforcement Learning, Tool Augmentation, Data Efficiency, Audio Routing

## 核心痛点
大型音频语言模型（LALMs）在细粒度听觉感知任务（如音高估计、事件计数）上表现不可靠，现有方法依赖数据密集型训练来内化感知能力，面临高标注成本和数据效率低下的挑战。

## 方法创新
提出AudioRouter框架：
- 使用强化学习（RL）将工具使用明确为离散决策问题，优化轻量级路由策略。
- 路由模块决定是否调用外部音频工具（如音高跟踪、事件检测工具），并选择具体工具，同时保持基础音频推理模型冻结。
- 通过相对结果奖励机制（比较使用工具和直接推理的性能）训练路由策略，无需手动标注工具使用标签。

## 实验结果
- 在标准音频理解基准上实现显著性能改进。
- 学习工具使用所需训练数据减少高达600倍，相比传统端到端训练范式更高效。
- 在多个设置中达到最先进结果。

## 一句话评价
AudioRouter通过强化工具使用决策，为音频理解提供了一个数据高效且可扩展的替代方案，避免了对感知能力内化的依赖。

---

## 9. Frame-Level Internal Tool Use for Temporal Grounding in Audio LMs

**作者**: Joesph An, Phillip Keung, Jiaqi Wang, Orevaoghene Ahia, Noah A. Smith
**链接**: [2602.10230](https://arxiv.org/abs/2602.10230)
**分类**: Audio Understanding | **关键词**: frame-level internal tool use, temporal grounding, audio language models, inhomogeneous Poisson process, word alignment, speaker diarization

# 论文总结: Frame-Level Internal Tool Use for Temporal Grounding in Audio LMs

## 核心痛点
音频语言模型在处理需要精确时间定位的任务（如词对齐、说话人分离）时面临以下问题：
- **幻觉问题**：标准方法生成时间戳作为文本令牌序列，容易产生与音频内容无关的输出。
- **计算效率低**：文本生成过程自回归，导致高计算成本。
- **长度泛化差**：模型在训练分布外的音频持续时间上表现不佳，容易出现大误差。

## 方法创新
论文提出“frame-level internal tool use”方法：
- **内部工具使用**：训练音频语言模型利用其内部音频表示直接执行时间定位，避免文本生成。
- **轻量级预测机制**：通过两种损失函数训练：
  - 二元帧分类器：预测每个帧是否包含目标事件。
  - 非均匀泊松过程（IHP）损失：建模时间事件强度，处理稀疏和依赖事件。
- **直接时间戳提取**：使用确定性函数（如峰值检测）从概率分布中提取时间戳，提高效率。

## 实验结果
在多个任务上评估：
- **任务**：词定位、说话人分离、音频事件定位。
- **性能**：优于基于令牌的基线方法，IHP损失通常表现更好。
- **效率**：推理速度提升超过50倍，仅需单次并行处理音频帧。
- **泛化能力**：在分布外音频持续时间上保持高准确性，显著减少幻觉。

## 一句话评价
该方法通过内部工具使用，有效提升了音频语言模型在时间定位任务中的准确性和效率，克服了标准文本生成方法的局限性。

---

## 10. MerkleSpeech: Public-Key Verifiable, Chunk-Localised Speech Provenance via Perceptual Fingerprints and Merkle Commitments

**作者**: Tatsunori Ono
**链接**: [2602.10166](https://arxiv.org/abs/2602.10166)
**分类**: Audio Watermarking and Provenance | **关键词**: speech provenance, perceptual fingerprints, Merkle tree, public-key verifiable, audio watermarking

### 核心痛点
现有语音起源系统面临主要挑战：神经水印系统如AudioSeal虽能实现鲁棒和本地化检测，但缺乏第三方可验证的加密证明将特定时间片段与发行者签名原始内容绑定；而C2PA等起源标准使用签名清单和Merkle碎片验证，但在重编码或常规分布处理下易失效。实际工作流涉及拼接、裁剪和平台级变换，需要系统在分布变换后保持有效性，并支持分块本地化验证。

### 方法创新
MerkleSpeech提出一种创新系统规范，结合四个组件：确定性分块指纹、基于Merkle树的承诺、发行者签名和紧凑带内水印负载。提供两个验证层级：WM-only层，仅依靠水印负载恢复，在常见分布变换下提供鲁棒归因；MSv1层，结合Merkle包含证明和签名，提供严格完整性保证。系统使用短语音分块计算感知指纹，构建Merkle树，签名根，嵌入负载以检索证明，实现公开信息验证。输出为拼接感知的时间线，指示各区域通过哪一层级及失败原因。

### 实验结果
论文描述了实验目标和设置：针对极低假阳性率进行评估，测试在重采样、带通滤波和加性噪声下的鲁棒性，并考虑神经编解码器作为主要压力因素。实验使用非重叠分块（L=S=2.0秒），指纹选项包括基于MFCC的严格指纹和SSL嵌入二值化，以实现不同鲁棒性-完整性权衡。实验目标旨在验证本地化拼接和鲁棒性类别。

### 一句话评价
该研究提出了一种实用的语音起源验证系统，巧妙结合稳健水印和加密证明，适用于真实分布变换场景，为分块处理和第三方验证提供了创新解决方案。

---

## 11. Emotion-Coherent Speech Data Augmentation and Self-Supervised Contrastive Style Training for Enhancing Kids's Story Speech Synthesis

**作者**: Raymond Chung
**链接**: [2602.10164](https://arxiv.org/abs/2602.10164)
**分类**: Text-to-Speech | **关键词**: Speech Synthesis, Data Augmentation, Self-Supervised Learning, Contrastive Learning, Emotion Recognition, Kids' Story

## 核心痛点
表达性语音合成需要生动的韵律和时机正确的停顿，但当前文本转语音（TTS）模型在处理长音频时面临挑战，特别是训练数据稀缺（如儿童故事书数据集较小），导致自然性和表达性不足。

## 方法创新
1. **情感一致的数据增强**：使用微调的情感文本分类器（基于自监督文本模型，如T5）识别句子情感，并合并情感匹配的音频以生成增强的长期语音数据，丰富训练资源。
2. **自监督对比风格训练**：应用SimCLR框架进行对比学习，通过随机掩码音频段创建不同视图，训练全局风格令牌（GST）模块提取更一致的说话风格嵌入。
3. **停顿建模**：在数据增强中模拟句子间停顿，基于真实数据拟合正常分布（均值为509ms，标准差为223ms），使模型学习自然的停顿模式。

## 实验结果
在Blizzard Challenge 2017数据集上评估，与使用连续两句子音频训练的基线模型相比，提出的方法在主观评估中自然性和风格适用性得分更高，且合成的语音在句子间停顿分布上更接近真实语音。数据统计显示，增强后训练数据量增加，提升了模型性能。

## 一句话评价
该方法通过创新的数据增强和对比训练策略，显著增强了儿童故事语音合成的表达性和自然性，为资源有限的表达性TTS提供了有效解决方案。

---

