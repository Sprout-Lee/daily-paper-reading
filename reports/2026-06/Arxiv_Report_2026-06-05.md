# Arxiv Daily Deep Report - 2026-06-05

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 31
---

## 1. USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding

**作者**: Heng-Jui Chang, Alexander H. Liu, Saurabhchand Bhati, Mrudula Athi, Anton Ratnarajah, Amit Chhetri, James Glass
**链接**: [2606.06444](https://arxiv.org/abs/2606.06444)
**分类**: Audio Representation Learning | **关键词**: audio representations, self-supervised learning, audio large language models, knowledge distillation, domain-aware distillation, depth scaling

## 核心痛点
现有音频编码器多针对单一领域（如语音、通用音频、音乐），缺乏能同时覆盖多领域的通用编码器。自监督模型（SSL）在跨域任务上表现不佳，而近期研究表明有监督编码器更适合音频大语言模型（LLM）。

## 方法创新
1. **域感知蒸馏**：根据输入音频的领域（语音/通用音频/音乐）动态调整各教师模型的蒸馏权重，避免等权重混合。
2. **引入音乐领域专家**：新增音乐SSL教师（MuQ）及音乐数据，弥补USAD在音乐任务上的不足。
3. **两阶段蒸馏**：第一阶段从三个SSL专家（WavLM、ATST-Frame、MuQ）蒸馏；第二阶段从有监督专家（Whisper Large-v3、Audio Flamingo 3）蒸馏，对齐下游LLM应用。
4. **高效规模扩展**：降低帧率（50Hz→25Hz）减少计算量，通过深度缩放（复制层）将模型参数提升至1B，避免从头训练。

## 实验结果
- 在HEAR、MARBLE、XARES-LLM三个基准上，USAD 2.0/2.0+在同类规模模型中达到SOTA或竞争性表现。
- 域感知蒸馏对语音、声音、音乐任务均有效（α=10最优）。
- 规模扩展（XXLarge+，1.036B参数）进一步提升性能。

## 一句话评价
USAD 2.0通过域感知蒸馏和多阶段知识迁移，构建了首个同时覆盖语音、通用音频和音乐的高效通用音频编码器，并成功扩展至十亿参数。

---

## 2. Revisiting Lexicon Evaluation in Unsupervised Word Discovery

**作者**: Simon Malan, Danel Slabbert, Herman Kamper
**链接**: [2606.06183](https://arxiv.org/abs/2606.06183)
**分类**: Zero-resource Speech Processing / Unsupervised Word Discovery | **关键词**: unsupervised word discovery, lexicon evaluation, normalized edit distance, clustering metrics, zero-resource speech processing

## 核心痛点
现有归一化编辑距离(NED)评估无监督词发现中的词典质量时，存在大簇偏向：NED对所有簇内单位对等权重平均，导致大簇质量主导分数，难以公平评估。此外，NED仅衡量同质性(Homogeneity)，忽略了类别如何分布在簇中(完备性)。

## 方法创新
1. **加权NED(Weighted NED)**：按簇大小加权平均簇内编辑距离，消除大簇偏向。
2. **逆度量(Inverse Metrics)**：衡量一个真实类别的样本分散到多少个簇中，对应完备性。
3. **音素错误率(PER)及其逆度量**：更快速的替代方案，计算簇内众数字串与各单位间的错误率。

## 实验结果
通过合成和真实词典实验，所提度量组合(加权NED+逆度量)与词典真实分布的相似性相关性更高，且对导致评估偏差的因素更鲁棒。与标准NED+比特率组合相比，新度量更能准确反映词典质量。

## 一句话评价
该文指出标准NED的缺陷，提出更公平、更全面的词典评估度量，对零资源语音处理领域具有重要意义。

---

## 3. CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer's Disease Detection

**作者**: Yin-Long Liu, Yuanchao Li, Yiming Wang, Yue Li, Rui Feng, Jiaxin Chen, Shaobo Liu, Liu He, Yuang Chen, Jiahong Yuan, Zhen-Hua Ling
**链接**: [2606.06170](https://arxiv.org/abs/2606.06170)
**分类**: Text-to-Speech, Alzheimer's Disease Detection, Data Augmentation | **关键词**: Alzheimer's disease detection, text-to-speech, data augmentation, automatic speech recognition, cognitive-state-conditioned TTS

## 核心痛点
基于语音的阿尔茨海默病（AD）检测受限于病理语音数据稀缺。传统数据增强方法（如噪声注入、音调变换）仅生成现有录音的变体，无法引入新的语义内容或显式建模病理特有的说话特征（如AD式不自然停顿）。

## 方法创新
提出**CoSTA**框架，包含四个组件：
1. **认知状态条件TTS模型**：基于CosyVoice2和F5-TTS，通过指令微调或引入认知标签，分别合成具有AD和健康对照（HC）特征的语音。
2. **多样化转录本池**：构建包含人工转录本（MT）和36种ASR转录本的池子，研究文本来源对TTS增强的影响。
3. **数据增强策略**：包括基于自参考和类内交叉合成的训练增强，以及测试时增强（TTA）。
4. **AD检测模型**：基于WavLM的语音检测模型。

## 实验结果
在ADReSS数据集上，CoSTA实现了85.83%的音频-only准确率，相比基线提升4.16%。实验表明ASR驱动的增强常优于MT驱动。

## 一句话评价
通过认知状态条件TTS合成病理语音并结合ASR转录本多样性，有效缓解了数据稀疏问题，显著提升AD检测性能。

---

## 4. VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization

**作者**: Xiao-Hang Jiang, Yang Ai, Rui-Chen Zheng, Li-Rong Dai, Zhen-Hua Ling, Ji Wu
**链接**: [2606.05892](https://arxiv.org/abs/2606.05892)
**分类**: Speech Coding | **关键词**: neural speech codec, voicing attribute, quantization, low bitrate, streamable

## 核心痛点
现有神经语音编解码器大多采用统一的逐帧量化策略，为所有帧分配相同比特率，未考虑语音内容特性（如浊音/清音），导致清音帧浪费比特，限制了低比特率下的性能。

## 方法创新
提出 VoCodec，一种基于浊音驱动的低比特率流式神经语音编解码器。核心组件包括：
- **浊音检测器**：利用帧能量在基频范围内的累积判断浊音/清音，输出浊音标志令牌。
- **浊音驱动量化器**：对浊音帧采用残差标量-矢量量化（RSVQ），对清音帧采用简单标量量化（SQ），实现比特率自适应分配。
- **掩码高效训练**：采用双路径并行量化和掩码机制加速训练。
整体架构基于 StreamCodec 的全因果编解码器，以 MDCT 谱为建模目标。

## 实验结果
- LibriTTS 16kHz 下，1.1 kbps 比特率时，VoCodec 在 LSD、STOI、ViSQOL、MUSHRA 指标上均优于 DAC、BigCodec、AudioDec、MDCTCodec-S、StreamCodec 等基线。
- 相比统一量化策略，引入浊音驱动量化可降低约 27% 比特率。
- VCTK 48kHz 下，2.7 kbps 时也取得最佳或次优结果。
- ABX 测试显示，VoCodec 在 1.1 kbps 下显著优于多数基线。

## 一句话评价
VoCodec 通过感知驱动的浊音自适应比特分配，在极低比特率下实现高质量流式语音编解码，具有实用价值。

---

## 5. An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

**作者**: Xiao-Hang Jiang, Yang Ai, Fei Liu, Rui-Chen Zheng, Jian-Qing Gao, Zhen-Hua Ling, Ji Wu
**链接**: [2606.05876](https://arxiv.org/abs/2606.05876)
**分类**: Speech Compression | **关键词**: neural speech codec, plain-to-pseudo synergistic vector quantizer, token prediction, ultra-low bitrate, P2PSynCodec

## 核心痛点
现有神经语音编解码器（如RVQ）在超低比特率（如0.5 kbps）下性能急剧下降，后级VQ贡献小却消耗相同比特率，导致效率低下。

## 方法创新
提出P2PSynCodec，核心是Plain-to-Pseudo协同向量量化器（P2PSVQ）：
- **Plain VQ**：量化产生基本token，用于传输（计入比特率）。
- **多个Pseudo VQ**：基于基本token通过神经网络预测辅助token，不消耗比特率。
- 解码时，基本token与预测的辅助token联合重建语音，大幅降低比特率。
- 训练采用两阶段：先训练RVQ教师模型，再固定编码器/解码器/Plain VQ，用交叉熵损失训练Pseudo VQ。

## 实验结果
- 在0.5 kbps（16 kHz）比特率下，重建质量与2.0 kbps的竞争编解码器相当，比特率降低75%。
- 在LibriTTS和VCTK数据集上，客观指标（UTMOS、ViSQOL等）和主观测试（MUSHRA、ABX）均表明性能优于或接近高比特率方法。
- 模型复杂度低（FLOPs和参数量适中）。

## 一句话评价
通过零比特率伪向量量化预测，在极低比特率下实现了高质量语音重建，为超低带宽场景提供了高效解决方案。

---

## 6. M2S-AVSR: Modality-aware Multi-view Self-supervised Representation for Robust Audio-Visual Speech Recognition

**作者**: Fei Su, Cancan Li, Juan Liu, Ming Li
**链接**: [2606.05763](https://arxiv.org/abs/2606.05763)
**分类**: Audio-Visual Speech Recognition | **关键词**: Audio-Visual Speech Recognition, Multi-view Representation Learning, Modality-aware Fusion, Self-supervised Learning, Robust Speech Recognition

## 核心痛点
真实场景下音频-视觉语音识别（AVSR）面临视角变化、音频失真、视觉遮挡等问题，导致模态质量下降和音视频异步，现有方法鲁棒性不足。

## 方法创新
1. **多视角自监督视觉表示学习**：利用真实和合成视角学习视角不变性表示。
2. **模态感知融合机制**：显式建模模态质量和跨模态同步性，实现细粒度门控融合。
3. **AISHELL8-RealScene数据集**：公开多场景、多视角真实环境音视频数据集。

## 实验结果
- 在LRS3上视角变化和视觉退化设置下相对提升29.4%。
- 在MISP2021-AVSR测试集上达到新SOTA。
- 在AISHELL8-RealScene室外场景取得最佳结果。

## 一句话评价
提出了一种结合多视角自监督学习和模态感知融合的鲁棒AVSR框架，在多种挑战性条件下显著提升性能。

---

## 7. Enhancing Audio Captioning with Auxiliary AudioSet Semantics

**作者**: Shubham Gupta, Adarsh Arigala, Sri Rama Murty Kodukula
**链接**: [2606.05717](https://arxiv.org/abs/2606.05717)
**分类**: Automatic Audio Captioning | **关键词**: Automated Audio Captioning, AudioSet, Auxiliary Information, Cross-Modal Learning, LLMs

## 核心痛点
自动音频字幕（AAC）面临词选择不确定性和对大规模序列到序列或LLM模型的依赖，限制了实际部署。现有方法虽利用辅助标签或主题先验，但往往依赖复杂解码器或多编码器管道，未系统分析语义指导与模型效率之间的权衡。

## 方法创新
提出一个资源高效的AAC框架，显式地基于预测的AudioSet语义进行字幕生成。具体包括：
- **音频编码器**：使用在AudioSet上预训练的ConvNeXt-Tiny提取帧级声学特征。
- **关键词模块**：用另一个冻结的ConvNeXt-Tiny分类器预测前K个AudioSet关键词，并将词嵌入拼接至声学特征后形成联合表示。
- **语言解码器**：采用紧凑的自定义六层BART风格解码器（3个编码器层和3个解码器层），在联合声学-语义条件下自回归生成字幕。
该方法在减少解码器容量需求的同时提升了语义连贯性和跨域鲁棒性。

## 实验结果
在Clotho V2和AudioCaps上进行了域内和跨域评估。主要结果（SPIDEr/FENSE）：
- Clotho域内：0.286/0.478（优于所有紧凑方法）
- AudioCaps域内：0.470/0.615（优于大多数基线）
- 跨域设置下也表现出竞争性能。
与大型预训练方法（如Pengi）相比，在保持竞争力的同时大幅降低了模型复杂度。

## 一句话评价
本文通过融合预测的AudioSet关键词作为显式语义指导，在紧凑架构下实现了高效且高质量的音频字幕生成。

---

## 8. Age-Aware Adapter Tuning for Children's Speech Recognition

**作者**: Jialu Li
**链接**: [2606.05440](https://arxiv.org/abs/2606.05440)
**分类**: Speech Recognition | **关键词**: 儿童语音识别, 适配器调优, 参数高效适应, 年龄感知适应, 年龄专用适配器, FiLM条件化

## 论文总结

### 核心痛点
儿童自动语音识别（ASR）面临挑战：儿童语音与成人差异大，且在不同发育阶段（3-12岁及以上）变化显著。现有的单一共享适配器无法充分捕捉年龄相关的声学变异，导致不同年龄组的词错误率（WER）存在较大差距。

### 方法创新
1. **年龄专用适配器（Age-Specialized Adapters）**：为四个年龄组（3–4/未知、5–7、8–11、12+）分别训练轻量级瓶颈适配器（bottleneck dimension=32），通过年龄路由器（基于第四层适配器特征的轻量FFN）在推理时选择适配器。
2. **统一年龄条件FiLM适配器（Unified Age-Conditioned FiLM Adapter）**：共享一个适配器，通过年龄嵌入（one-hot或路由器预测分布）进行特征线性调制（FiLM），年龄门控控制条件化强度。
3. **年龄路由器**：使用mean-pooled第四层适配器特征训练，推理时预测年龄组，实现无真值年龄标签的年龄感知适配。

### 实验结果
- 在On Top of Pasketti儿童ASR挑战赛数据上，年龄专用适配器（使用真值年龄路由）相比共享儿童适配器基线，整体WER从12.6%降至12.3%，宏平均WER从18.4%降至17.6%。所有年龄组均有一致改善。
- 预测年龄路由接近真值路由性能（整体WER 12.3%，宏WER 17.8%），无需推理时年龄标签。
- 统一FiLM适配器增益较小，表明单一适配器难以捕捉发育变异。

### 一句话评价
本文首次系统研究年龄感知适配器调优在儿童ASR中的应用，证明年龄专用适配器优于统一条件适配器，且预测年龄路由可行。

---

## 9. F3-Tokenizer: Taming Audio Autoencoder Latents for Understanding and Generation

**作者**: Dinghao Zhou, Xingchen Song, Di Wu, Pengyu Cheng, Shengfan Shen, Sixiang Lv
**链接**: [2606.06357](https://arxiv.org/abs/2606.06357)
**分类**: Audio Tokenizer / Audio Representation Learning | **关键词**: Audio Tokenizer, Continuous Latents, Representation Learning, Flow Matching, Autoregressive Generation, Normalized Autoencoder, RQ-MTP, Frozen LLM

### 核心痛点
现有音频表示方法难以同时支持理解与生成：连续自编码器重建好但潜在表示结构弱，自监督编码器有语义但不可解码。

### 方法创新
提出 **F3-Tokenizer**，包含两个组件：
1. **归一化自编码器瓶颈**：使用通道归一化和随机扰动替代KL正则化，产生尺度可控的连续潜在表示，用于重建和自回归生成。
2. **潜在侧表示编码器**：在冻结的自编码器潜在表示上，使用随机量化多令牌预测（RQ-MTP）和冻结LLM监督训练，产生高维表示用于理解。
此外，训练一个补丁级流头，将LLM状态映射到连续自编码器潜在补丁，实现生成可控。

### 实验结果（论文截断部分未提供）
暂无。

### 一句话评价
F3-Tokenizer通过归一化连续瓶颈和表示编码器，统一了音频理解与生成中的表示，避免了额外编码器或离散码本，保持了自编码器潜在作为声学锚点。

---

## 10. FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition

**作者**: Fernando López, Santosh Kesiraju, Jordi Luque
**链接**: [2606.06211](https://arxiv.org/abs/2606.06211)
**分类**: Speech Recognition | **关键词**: pathological speech recognition, speaker conditioning, parameter-efficient adaptation, FiLM, x-vector, dysarthria

# FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition

## 核心痛点
病理语音（如ALS、帕金森病导致的语言障碍）与正常语音存在声学失配，导致传统ASR系统性能显著下降。病理语音数据集稀缺且说话人多样性有限，尤其是在非英语语言（如西班牙语）中，数据饥饿的微调策略易过拟合。

## 方法创新
提出基于FiLM（Feature-wise Linear Modulation）的说话人条件化策略，将x-vector说话人嵌入注入到冻结的ASR编码器每个Transformer层，通过线性缩放和偏移调节内部表示，而不修改基模型权重。具体包括：
1. 使用预训练的多语言SiAmResNet34提取x-vector，对健康语音掩码为零向量。
2. 每个编码器层有独立的FiLM生成器（两层MLP），输出仿射参数γ、β和标量门控α。
3. 门控残差调制：H̃ = H + α(γ-1)⊙H + β。
4. 训练仅更新FiLM生成器和说话人提取器（约1.6%参数）。

## 实验结果
- 在NeuroVoz（西班牙语）和TORGO（英语）病理语音上评估，与全微调（FFT）、编码器微调（EFT）、LoRA等方法对比。
- 说话人条件化ASR在WER上与已有适配策略竞争，同时保留对非条件语音的性能。
- 在MCQA（性别、年龄）任务上，说话人条件化几乎不损失基模型的语音理解能力。

## 一句话评价
本文提出一种轻量级、非破坏性的说话人适应方法，通过FiML在不改变预训练权重的前提下有效提升病理语音识别性能，并保持泛化能力。

---

## 11. Learning Emotion-discriminative Representations for Zero-Shot Cross-lingual Speech Emotion Recognition

**作者**: Jinyi Mi, Ding Ma, Tomoki Toda
**链接**: [2606.06200](https://arxiv.org/abs/2606.06200)
**分类**: Cross-lingual Speech Emotion Recognition | **关键词**: zero-shot cross-lingual speech emotion recognition, supervised contrastive learning, speaker adversarial learning, emotion-discriminative representations, language-invariant representations

### 核心痛点
零样本跨语言语音情感识别面临两大挑战：跨语言分布不匹配以及目标语言缺乏情感标注。传统基于监督迁移学习的方法需要目标语言标签，无监督方法虽不依赖标签但常利用目标语言数据或语言标签，且未能显式建模跨语言情感类别结构一致性。

### 方法创新
提出一种情感判别表征学习方法，融合监督对比学习（Supervised Contrastive Learning）与说话人对抗学习（Speaker Adversarial Learning）。监督对比学习通过语言感知加权（language-aware weighting）增强跨语言情感对齐，而说话人对抗学习通过梯度反转层（GRL）抑制说话人相关线索，促使模型学习说话人不变的表征。此外，采用层次化跨语言采样策略（hierarchical cross-lingual sampling）构建对比批次，确保多种语言和情感类别的共存。

### 实验结果
在9个零样本跨语言设置（如EN→DE、CN→FR等）下进行实验，使用UAR和Macro-F1评估。提出的方法（Proposed）显著优于两个基线（Baseline 1、Baseline 2）及其消融变体（Proposed w/o L_SupCLR、Proposed w/o L_SpkAdv）。消融实验证实了两个损失项的有效性。可视化表征空间显示情感类别聚类更紧凑，跨语言情感对齐更佳。

### 一句话评价
该工作通过显式对齐跨语言情感表征并解耦说话人信息，以少量语言训练数据实现了成本高效的零样本跨语言语音情感识别。

---

## 12. Multi-task Learning is Not Enough: Representational Entanglement in Dual-output Second Language Speech Recognition

**作者**: Seung Hwan Cho, Young-Min Kim
**链接**: [2606.06065](https://arxiv.org/abs/2606.06065)
**分类**: Speech Recognition | **关键词**: Multi-task Learning, Representational Entanglement, Dual-output ASR, Second Language Speech Recognition, Conformer, CKA analysis

### 核心痛点
论文指出在多任务学习（MTL）框架下，针对第二语言（L2）语音识别的双输出（表面转录和意义转录）任务存在不对称性：MTL提升意义转录性能，但导致表面转录退化，且退化程度随语言和表面-意义差异（编辑距离）变化。英语中的退化比韩语更严重，原因在于编码器级别的表征纠缠。

### 方法创新
- 对比单输出（SO）和双输出（DO）模型，采用Conformer编码器+Transformer解码器架构。
- DO模型共享编码器，两个独立解码器分别输出表面和意义转录，并加入辅助CTC损失。
- 通过中心核对齐（CKA）分析编码器和解码器的表征相似性，定位性能差异的根源。

### 实验结果
- 韩语：SO模型表面CER 11.14%，意义1.60%；DO模型表面CER 11.34%（退化），意义0.77%（提升）。
- 英语：SO模型表面CER 13.78%，意义3.87%；DO模型表面CER 15.08%（显著退化），意义3.19%（提升）。
- 分层分析显示：韩语编码器为不同任务学习不同表征，而英语编码器表征高度相似（纠缠）。解码器层面，韩语DO解码器保持任务特异性，英语DO意义解码器退化。

### 一句话评价
论文系统地揭示了多任务学习在双输出L2语音识别中的表征纠缠问题，并分析了语言依赖机制，为设计解纠缠的MTL框架提供了重要见解。

---

## 13. SpeechJBB: Probing Safety Alignment and Comprehension in Large Audio Language Models under Code-Switched Speech

**作者**: Virginia Ceccatelli, Yejin Jeon, David Ifeoluwa Adelani
**链接**: [2606.06037](https://arxiv.org/abs/2606.06037)
**分类**: Audio Language Model Safety | **关键词**: Jailbreak, Code-switching, Safety Alignment, Large Audio Language Models, Obfuscation, Multilingual Safety

## 核心痛点
现有大型音频语言模型（LALMs）的安全对齐评估主要基于单语言文本有害提示，忽略了多语言和口语场景，尤其是代码切换语音下的泛化能力。

## 方法创新
1. 提出首个音频代码切换越狱数据集 SpeechJBB，涵盖100个有害和100个良性提示，翻译成德语、西班牙语、法语、意大利语并合成语音，同时生成10个代码切换语言对。
2. 引入增强设置：在安全关键术语周围插入音韵学上合理的伪词，模拟局部混淆，测试三种插入比例（10%、30%、50%）。
3. 使用GPT-4.1作为评估裁判，将模型响应分类为拒绝、回避和越狱。

## 实验结果
- 代码切换有害音频显著提高了越狱成功率（JSR），非英语单语和非英语代码切换对表现出最高的攻击成功率。
- 伪词插入进一步降低了拒绝率，表明自然发音的混淆能有效绕过安全策略。
- 评估了9个最先进的LALMs（包括开源和商业模型），展示了多语言和多模态对齐框架的严重漏洞。

## 一句话评价
首项系统研究代码切换语音对LALMs安全对齐的影响，揭示了现有安全机制在多语言口语输入下的脆弱性。

---

## 14. To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection

**作者**: Erfan Loweimi, Mengjie Qian, Kate Knill, Guanfeng Wu, Chi-Ho Chan, Abbas Haider, Muhammad Awan, Josef Kittler, Hui Wang, Mark Gales
**链接**: [2606.05931](https://arxiv.org/abs/2606.05931)
**分类**: Audio-Visual Person Retrieval | **关键词**: multimodal retrieval, active modality detection, speaker embedding, face embedding, query-adaptive fusion

## 核心痛点
实际广播视频档案中，目标人物可能出现声音但未见画面（Audio-only）、画面但未说话（Visual-only）、或两者兼有。固定多模态融合会因无效模态引入噪声，性能甚至低于最佳单模态系统。

## 方法创新
提出查询自适应框架，包含**活跃模态检测**模块：
1. 基于跨模态分数一致性（同一查询下，一个模态检索的top-n文件在另一模态下的分数分布）设计特征，结合模态内和模态间分数统计量。
2. 使用逻辑回归分类器（因数据有限）判断查询属于AoP、VoP或AVP。
3. 根据检测结果自适应设置融合权重λ（AoP:1, VoP:0, AVP:0.5）。

## 实验结果
在BBC Rewind语料库（12,594个视频）上：
- 模态检测准确率89%
- 自适应融合P@1达到94.2%，优于仅音频（82.9%）、仅视觉（93.4%）和固定融合（90.0%），恢复了与Oracle（96.6%）之间64%的差距。

## 一句话评价
通过跨模态分数一致性有效检测缺失模态，实现查询自适应融合，显著提升真实场景下音视频人物检索精度。

---

## 15. DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexity Monaural Speech Enhancement

**作者**: Cunhang Fan, Enrui Liu, Jing Zhou, Jian Kang, Jie Li, Andong Li, Jian Zhou, Zhao Lv, Xuelong Li
**链接**: [2606.05911](https://arxiv.org/abs/2606.05911)
**分类**: Audio Enhancement | **关键词**: Speech Enhancement, Deep Learning, Artificial Neural Network, Spiking Neural Network, Dual-Branch Hybrid Neural Network, Low-Complexity, Monaural Speech Enhancement, BandSplit, Mamba, TF-Cross Attention Fusion

## 核心痛点
当前基于人工神经网络（ANN）的语音增强方法虽然性能优异，但计算复杂度和能耗高，限制了在边缘设备上的部署。而脉冲神经网络（SNN）具有超低功耗潜力，但其离散二进制激活和复杂的时空动态导致信息丢失，性能下降。因此，如何在保持性能的同时降低计算复杂度成为关键挑战。

## 方法创新
提出了一种双分支混合神经网络（DBHN-Net），包含ANN分支和SNN分支。
- **网络架构**：双分支并行，ANN分支利用BandSplit模块和TF-Mamba模块（基于Mamba的时序建模）降低计算量；SNN分支引入Spiking Feature Extraction Group (SFEG) 和 Information Transformation Block (ITB)，通过残差连接减轻信息损失。
- **信息融合**：Interaction模块实现分支间渐进式信息交换；TF-Cross Attention-Fusion (TF-CAF) 模块通过时频双域交叉注意力进行最终融合，数据自适应地引导SNN分支保留关键信息。

## 实验结果
在三个公开数据集上，DBHN-Net保持优越性能，同时相比基线模型平均降低7.5倍计算复杂度（平均7.5倍减少）。

## 一句话评价
提出了一个创新的ANN-SNN双分支混合网络，通过架构设计、模块创新和融合机制，成功在低复杂度下实现了高性能语音增强。

---

## 16. Beyond WER: A Paired Acoustic Stress Test for Ambient Clinical Scribes

**作者**: Xiao-Hang Jiang, Han-Jie Guo, Ying-Si Liang, Yang Ai, Zhen-Hua Ling, Lei Jiang, Zhi-Yang He
**链接**: [2606.05909](https://arxiv.org/abs/2606.05909)
**分类**: Clinical Speech Processing | **关键词**: clinical speech processing, large language models, error propagation, patient safety, Word Error Rate, acoustic stress test, ambient noise, negation error, safety-critical error rate, ASR robustness

# Summary

## Core Problem
Traditional metrics like Word Error Rate (WER) mask systemic safety degradation in ambient clinical scribes (ASR + LLM pipelines). A small increase in WER can correspond to a large increase in unsafe clinical outputs, as WER is semantically unaware.

## Method Innovation
- **Paired Acoustic Stress Test**: For the same clinical dialogue, inject diverse noise types (stationary ambient vs. non-stationary semantic interference) at varying SNRs while keeping the downstream LLM configuration frozen.
- **Within-case design**: Clean and noisy versions of the same dialogue are compared, isolating the causal impact of acoustic perturbations on downstream clinical reasoning.
- **New taxonomy**: Links cause-side error triggers (negation flips, number/unit errors, non-speech pollution, temporal distortion) to result-side safety endpoints (triage drift, omitted red flags, false claims).
- **Evaluation metrics**: Beyond WER, they propose Negation Error Rate (NegErr), Triage Match, Under-Triage Rate, and Safety-Critical Error Rate (SCER) to directly measure clinical invariance.

## Key Results
- Stationary ambient noise (15 dB SNR) increased WER by only **0.71 percentage points**, but nearly **doubled the rate of unsafe outputs** (SCER).
- Minor acoustic perturbations (e.g., omission of "don't") can invert clinical meaning without substantially inflating WER.
- A lightweight mitigation strategy (without fine-tuning) effectively reduces safety degradation under noisy conditions.

## One-Sentence Evaluation
This paper exposes the dangerous disconnect between signal fidelity (WER) and clinical safety, and provides a principled framework (paired acoustic stress test) for evaluating robustness of ASR→LLM pipelines in healthcare, with actionable metrics that capture semantic safety drift.

---

## 17. GLASS: GRPO-Trained LoRA for Acoustic Style Steering in Zero-Shot Text-to-Speech

**作者**: Jaehoon Kang, Yejin Lee, Kyuhong Shim
**链接**: [2606.05889](https://arxiv.org/abs/2606.05889)
**分类**: Text-to-Speech | **关键词**: GLASS, GRPO, LoRA, Acoustic Style Control, Zero-Shot TTS, Reward-Guided Training, Adapter Arithmetic, Composable Control

## 核心痛点
传统零样本文本转语音（TTS）模型在给定说话人提示时，说话人身份与韵律属性（如语速、音高）紧密耦合，难以在不改变提示的情况下独立调节风格。现有可控TTS方法需要风格标签、参考样本或文本描述，缺乏连续插值和多轴组合能力。

## 方法创新
GLASS框架提出将每个声学属性视为奖励定义的控制方向。核心创新包括：
- **奖励引导的GRPO训练**：对每个控制轴，冻结TTS骨干网络，使用组相对策略优化（GRPO）训练单个轻量级LoRA适配器。奖励基于语音令牌长度（语速）、平均基频（音高）和词错误率（可懂度）。
- **LoRA算术实现组合**：独立训练的适配器可在推理时通过线性LoRA算术进行交换、插值和组合（如α∆Wfast + (1-α)∆Wslow），无需重新训练骨干。
- **说话人无关风格方向**：多说话人提示训练确保适配器可迁移至未见过的说话人。

## 实验结果
在Seed-TTS-eval test_en数据集上（N=1088），GLASS在语速和音高控制上达到与DSP处理相当的样式偏移，同时保持自然度、说话人相似度和可懂度（WER、SpkSim、UTMOS等指标优于DSP基线）。连续插值实验显示α从0到1可平滑调节语速（2.30→5.52 SPS）和音高（男声107→155 Hz，女声166→239 Hz），混合点α=0.5处WER最低。

## 一句话评价
GLASS通过GRPO学习可组合的LoRA风格适配器，实现了零样本TTS中无需标签的、说话人保持的连续风格控制。

---

## 18. UniVoice: A Unified Model for Speech and Singing Voice Generation

**作者**: Junjie Zheng, Huixin Xue, Shihong Ren, Chaofan Ding, Hao Liu, Zihao Chen
**链接**: [2606.05852](https://arxiv.org/abs/2606.05852)
**分类**: Text-to-Speech, Singing Voice Synthesis | **关键词**: 统一语音歌声生成, 条件流匹配, 因子化条件, 扩散Transformer, 空旋律令牌

## 核心痛点
传统TTS和SVS需要不同条件：语音依赖语言韵律，歌声需要显式旋律控制。统一模型易导致梯度冲突，降低生成质量。

## 方法创新
1. **因子化条件**：将条件分解为内容、旋律、音色，分别用专用编码器处理。歌声使用MIDI音符编码旋律，语音使用可学习的空旋律令牌，避免旋律约束。
2. **共享DiT骨干**：基于条件流匹配的扩散Transformer，无分离任务头，通过任务令牌调制适应不同模态。
3. **理论分析**：证明空旋律令牌近似于对旋律变量的边缘化，减少梯度冲突。

## 实验结果
- 语音PER: 5.26%（接近F5-TTS 5.21%和CosyVoice3 5.30%）
- 歌声PER: 16.22%（优于统一基线Vevo1.5的24.72%）
- 消融实验验证因子化条件和空旋律令牌的重要性。
- 发布UNISINGING-EVAL基准（12种音乐风格）。

## 一句话评价
UniVoice通过因子化条件和空旋律令牌巧妙解决语音与歌声统一生成中的条件冲突，性能媲美专用模型。

---

## 19. Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs

**作者**: Gio Paik, Hyunseo Shin, Soungmin Lee
**链接**: [2606.05846](https://arxiv.org/abs/2606.05846)
**分类**: Speech Recognition | **关键词**: code-switching, multilingual ASR, model merging, domain generalization, unseen language pairs

## 核心痛点
现有Code-Switching ASR（CS-ASR）方法主要针对已见语言对（如中英、韩英），但实际中语言对数量呈组合增长，收集所有配对的数据不可行。本文研究如何将从有限已见语言对（KO-EN、JA-EN、DE-EN）学到的CS能力泛化到未见语言对（KO-JA、KO-DE）。

## 方法创新
1. **模型合并**：将分别在已见语言对上微调得到的三个双语CS-ASR模型进行合并，采用Task Arithmetic、TIES-Merging、DARE三种策略。
2. **域泛化**：在已见语言对上使用Fish、Fishr、GGA-L等方法训练，直接评估在未见语言对上的表现。
3. **数据集构建**：为KO-JA和KO-DE创建了首个CS语音评估集（分别450和387条）。

## 实验结果
- 单一语言对微调对其他语言对有一定提升（例如JA-EN微调使KO-JA的MER从0.44降至0.31），但泛化有限。
- **模型合并**中，TIES表现最稳定：KO-EN+JA-EN合并后，在未见语言对KO-JA上MER达0.31（优于单独微调），但整体MER仍>0.3。
- **域泛化**中，Fishr效果最佳：未见语言对平均MER从0.41降至0.33，但仍不够实用。
- 三模型直接合并（Task Arithmetic/DARE）反而导致性能崩溃（MER升至0.77）。

## 一句话评价
本文首次系统验证了CS-ASR跨语言对泛化的可行性，但实验表明现有模型合并和域泛化方法仅能带来有限提升，亟需针对CS-ASR特性设计的新技术。

---

## 20. FORTE: FOL-guided Optimal Refinement for Text-audio rEtrieval

**作者**: Arghya Pal, Sailaja Rajanala
**链接**: [2606.05812](https://arxiv.org/abs/2606.05812)
**分类**: Text-to-Audio Retrieval | **关键词**: Text-to-Audio Retrieval, First-Order Logic, Multimodal Representation Learning, Query Refinement, Parameter-Efficient Fine-Tuning

## 核心痛点
现有的文本到音频检索方法（如CLAP、Pengi）因文本与音频之间的模态鸿沟，难以实现细粒度语义对齐，常返回语义不匹配的结果。

## 方法创新
提出FORTE框架，包含三个阶段：
1. **FOL引导的查询优化**：将自然语言查询转化为一阶逻辑（FOL）表示，通过约束搜索（最佳优先搜索）生成保留核心语义同时增强区分性的逻辑形式。
2. **参数高效跨模态对齐**：使用轻量级投影模块和对比学习，在不微调预训练编码器的情况下对齐音频嵌入到优化后的查询空间。
3. **谓词感知重排序**：在推理阶段利用逻辑一致性对检索结果进行重排序，消除残余不匹配。

## 实验结果
在AudioCaps和Clotho基准上，FORTE在细粒度场景下显著优于强基线方法，验证了符号推理与表示学习结合的有效性。

## 一句话评价
首次将一阶逻辑系统性地融入文本到音频检索流程，通过结构化语义推理提升了检索精度。

---

## 21. SagnacAssisted Enhanced OTDR for Distributed Acoustic Sensing: A Standardized Benchmark and Engineering Evaluation Framework

**作者**: Weiguang Wang, Fugen Wu, Hailing Wang, Xuechen Liang, Xiaobin Li, Ru Han, Tianchang Xie
**链接**: [2606.05754](https://arxiv.org/abs/2606.05754)
**分类**: Distributed Acoustic Sensing | **关键词**: Distributed Acoustic Sensing, Phase-sensitive optical time-domain reflectometry, Sagnac-assisted sensing, Benchmark evaluation, Channel grouping optimization

### 核心痛点
传统相位敏感光时域反射计（ϕ-OTDR）在分布式声学传感中易受偏振诱导衰落、局部信号退化及强环境干扰影响，导致性能不稳定。

### 方法创新
提出Sagnac辅助增强ϕ-OTDR架构，利用Sagnac干涉仪提供连续相位响应作为辅助传感源，补偿ϕ-OTDR信道的衰落区域；通过FPGA上的互相关过程实现异质信号对齐；建立标准化基准评估框架，对比传统特征工程、概率浅层分类器、单分支深度模型和双分支融合模型。

### 实验结果
在10km传感光纤上对六类代表性声学事件进行实验，双分支融合模型在平衡测试集上达到89.79%准确率、89.83%宏F1分数和5.00%虚警率。通道分组显著影响双分支评估，部署决策应基于准确率、宏F1、虚警率、漏报率和延迟等多指标。

### 一句话评价
该工作为ϕ-OTDR DAS提供了物理驱动的增强策略和可复现的基准协议，推动了融合传感方法的工程化评估。

---

## 22. Do speech foundation models perceive speaker similarity as humans do?

**作者**: Minoru Kishi, Hayato Yagi, Shinnosuke Takamichi, Yuki Saito
**链接**: [2606.05739](https://arxiv.org/abs/2606.05739)
**分类**: 说话人表示学习与感知分析 | **关键词**: speaker similarity, speech foundation models, perceptual similarity, embedding alignment, self-supervised learning

## 核心痛点
人类能够连续地感知说话人之间的相似度，但语音基础模型（如自监督模型和大规模监督模型）生成的说话人嵌入与人类感知是否一致尚不清楚。现有研究主要关注说话人验证（二分类），忽略了相似度的连续性。

## 方法创新
- 使用超过40个模型（包括ASR、TTS、TTA、音频分类、语音SSL、音频SSL等六类），提取各Transformer层的说话人嵌入。
- 定义三种度量指标衡量模型嵌入相似度与人类感知评分的对应关系：成对相似度相关系数（LCC/SRCC）、Frobenius距离（矩阵差异）、谱距离（图结构差异）。
- 进行多元回归分析，探究模型配置（是否解码器、是否多语言、是否自监督、训练数据量、参数量）对对齐程度的影响。

## 实验结果
- 模型间差异显著：WavLM系列在所有层上均与人类感知高度对齐，而Qwen3-TTS表现较差。
- 层间趋势多样：多数模型深层对齐度下降，但AudioGen和VALL-E X呈上升趋势。
- 回归分析表明：解码器结构、多语言训练、自监督学习、更大数据量和参数量通常有助于提升对齐。

## 一句话评价
该研究系统性地验证了语音基础模型的说话人嵌入与人类感知相似度之间的关联，为开发更符合人类感知的模型提供了指导。

---

## 23. Beyond Generative Decoding: Discriminative Hidden-State Readout from a Native Omni-Modal LLM for Multimodal Sentiment Analysis

**作者**: Bin Wen, Tien-Ping Tan
**链接**: [2606.05713](https://arxiv.org/abs/2606.05713)
**分类**: Multimodal Sentiment Analysis | **关键词**: Multimodal sentiment analysis, Large multimodal models, Qwen2.5-Omni, Parameter-efficient fine-tuning, Low-rank adaptation, Discriminative readout

## 核心痛点

当前多模态情感分析（MSA）通常使用生成式解码（generative readout）从大语言模型（LLM）中获取情感分数，即将分数作为文本字符串生成后解析为数字。这种方法将连续的回归目标与离散的自回归解码绑定，存在精度限制、推理延迟高、输出不可解析或越界等问题，且其成本未被充分量化。

## 方法创新

论文提出一种判别式隐状态读取（discriminative hidden-state readout）方法，基于原生全模态LLM Qwen2.5-Omni-7B的Thinker模块。具体地，丢弃生成头，取最后一个非填充token在最后一层的隐藏状态，通过轻量级多层感知机（MLP）直接回归连续情感分数，仅需一次前向传播。采用4位量化和低秩适应（QLoRA）微调，仅训练约1.14%的参数，使7B模型可在单张32GB消费级GPU上运行（峰值内存10-21GB）。通过受控对比实验（固定骨干网络、数据和LoRA配置，仅改变读取方式）确保改进归因于读取机制本身。

## 实验结果

在CMU-MOSI和CMU-MOSEI数据集上，判别式读取达到了与最新技术相当的性能（MOSI: MAE 0.551, Corr 0.888; MOSEI: MAE 0.506, Corr 0.790），且四项随机种子实验稳定性好（MOSI: MAE 0.570±0.014, Corr 0.877±0.009）。受控对比中，生成式读取的平均绝对误差超过两倍，存在约2.8%的不可解析零样本输出，且推理速度更慢。模态消融实验揭示了各模态的贡献。

## 一句话评价

本文揭示了在连续MSA任务中，如何从大语言模型中读取结果与如何训练同样重要，判别式读取是比生成式解码更准确、高效、可靠的替代方案。

---

## 24. SB-RF: Schrödinger Bridge Rectified Flow for One-Step Robust Speech Enhancement

**作者**: Caixia Lu, Xueyang Lv, Penglong Hu, Jiaming Xu
**链接**: [2606.05575](https://arxiv.org/abs/2606.05575)
**分类**: Speech Enhancement | **关键词**: speech enhancement, diffusion model, one-step generation, Schrödinger bridge, rectified flow

## 核心痛点
现有扩散模型在语音增强中需要多步推理（50-200步），推理速度慢；一步生成方法如MeanFlowSE依赖大规模预训练编码器（如WavLM-Large），计算成本高，难以部署。标准Rectified Flow（RF）采用确定性线性插值路径，无法捕捉语音信号的多模态后验分布，鲁棒性不足。

## 方法创新
提出SB-RF框架，融合Schrödinger Bridge（SB）与Rectified Flow（RF）：
- **SB**：将生成过程建模为熵正则化最优传输问题，构建数据自适应的随机“概率管”轨迹，替代RF的刚性线性路径，增强对复杂噪声的鲁棒性。
- **RF速度匹配**：在SB路径上使用RF的速度匹配目标（预测y-x），使轨迹在正则化消失时逼近最优传输测地线（直线），实现一步生成。
- **训练损失**：联合速度匹配损失、多分辨率Mel谱损失和PESQ损失，提升重构质量。
- **推理**：使用欧拉ODE求解器一步生成干净语音。

## 实验结果
- 在标准VoiceBank-DEMAND基准上达到生成方法中的领先性能。
- 在扩展的低信噪比（低SNR）测试集上表现出强鲁棒性和高效率，NFE=1。
- 不依赖外部预训练模型，适合设备端部署。

## 一句话评价
SB-RF通过将Schrödinger Bridge的随机最优传输路径与Rectified Flow的确定性速度匹配结合，实现了高质量、鲁棒、一步生成的语音增强。

---

## 25. Sound Effects Dataset Unification With the Universal Category System

**作者**: Jun Woo Beck, Alexander Lerch
**链接**: [2606.05571](https://arxiv.org/abs/2606.05571)
**分类**: Audio Dataset & Annotation | **关键词**: Universal Category System, Sound Effects, Dataset Unification, Tag Conversion, Data Merging

## 核心痛点
现有音效（SFX）数据集采用不同标签体系、分类法和元数据格式，导致不兼容、不可比、难以合并等问题。

## 方法创新
提出一个模块化数据集重新标注框架，基于行业标准 Universal Category System (UCS) 作为共享结构。包含：
- 基于规则的多阶段标签转换流水线（预定义映射、子类别匹配、类别匹配、同义词搜索）
- 冲突解决机制（特异性过滤、多数投票、位置优先级）
- UCS感知的分层数据集拆分工具
- 支持多数据集合并

## 实验结果
在 AudioSet、FSD50K、ESC-50 三个数据集上转换，生成 EnvSound-UCS 数据集，包含 58,057 个音频片段。自动转换率高，需要最少人工干预。

## 一句话评价
通过引入工业标准UCS，有效统一了非兼容的音效数据集标注，促进了数据集互操作性和扩展性。

---

## 26. Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs

**作者**: Huu Tuong Tu, Hanh Nguyen, Thien Van Luong, Nguyen Tien Cuong, Vu Huan, Nguyen Thi Thu Trang
**链接**: [2606.05569](https://arxiv.org/abs/2606.05569)
**分类**: Mispronunciation Detection and Diagnosis | **关键词**: Mispronunciation detection and diagnosis, language-specific statistical graphs, computer-assisted pronunciation training, graph neural network, L2-ARCTIC

## 核心痛点
传统MDD系统使用语言无关的图结构（如分类图）建模发音错误，无法捕捉不同母语（L1）背景下的系统性混淆模式，且分类图忽略跨类别混淆、等权连接、无方向性等问题。

## 方法创新
1. 提出**统计混淆图**：从训练数据中统计每对音素的替换频率，构建有向加权图，边缘权重为条件概率，准确反映真实错误模式。
2. 引入**语言特定统计图（LSSG）**：为每个L1群体单独构建统计图，通过GCN生成L1自适应的音素嵌入，在语言编码器中动态选择对应图，使模型学习母语依赖的发音偏差。
3. 整体框架MDD-LSSG：采用wav2vec2音频编码器 + GCN语言编码器 + 交叉注意力融合，输出CTC预测。

## 实验结果
在L2-ARCTIC数据集上，F1-score达59.52%，优于L1-aware基线（56.83%）和分类图方法（CAT-GCN-MDD 58.12%），验证语言特定统计图的有效性。

## 一句话评价
通过数据驱动的方式为不同母语群体构建统计混淆图，显著提升了MDD的检测与诊断性能。

---

## 27. Probing Spatial Structure in Pretrained Audio Representations

**作者**: Chuyang Chen, Sivan Ding, Adrian S. Roman, Juan Pablo Bello
**链接**: [2606.05544](https://arxiv.org/abs/2606.05544)
**分类**: Audio Representation Learning | **关键词**: spatial audio, representation learning, probing, benchmark, SARL, linear probing, source localization, room acoustics

## 核心痛点
现有音频表示基准（如HEAR, SUPERB, MARBLE）主要关注单声道和语义任务，缺乏对空间信息的系统评估；任务导向的基准（如DCASE, LOCATA）将表示质量与下游架构、监督信号、训练策略混杂，难以隔离空间编码能力。

## 方法创新
提出Spatial Audio Representation Learning (SARL)基准，通过**控制仿真**构建平衡空间声学场景数据集，覆盖源级（方位角、仰角、距离、事件类别）和房间级（RT60、体积、形状）因素。采用**统一线性探针协议**，在冻结编码器上训练轻量分类器，实现架构无关的比较。此外，引入**敏感性分析**，通过扰动源或房间因素测量嵌入的几何响应。

## 实验结果
对14个预训练编码器（单声道、立体声、双耳、FOA格式，涵盖自监督、监督、编解码器范式）进行评估，发现：
- 输入格式和训练范式显著影响空间编码能力，多通道（尤其是FOA）模型整体更优。
- 源级因素（方位角、距离、类别）的系统解码难度始终低于房间级因素（RT60、体积、形状）。
- 敏感性分析显示，表示对不同因素（源vs房间）的扰动呈现异质性响应，房间因素变化对嵌入影响更大。

## 一句话评价
该工作通过控制探针范式系统性揭示了当前预训练音频表示对空间信息的编码偏好与偏差，为空间表示学习提供了标准化评估工具。

---

## 28. Exploring LLMs for South Asian Music Understanding and Generation

**作者**: Faria Binte Kader, Mohtasim Hadi Rafi, Shah Wasif Sajjad, Santu Karmaker
**链接**: [2606.05522](https://arxiv.org/abs/2606.05522)
**分类**: Music Understanding and Generation | **关键词**: Large Language Models, South Asian classical music, music understanding, music generation, raga, tala, ABC notation, benchmark, prompting framework

## 核心痛点
当前LLMs在音乐理解与生成方面主要聚焦于西方调性传统，对结构迥异、低资源的非西方音乐传统（如南亚古典音乐）缺乏系统评估。现有基准和生成框架无法捕捉基于拉格（raga）、塔拉（tala）的旋律与节奏约束。

## 方法创新
1. **南亚音乐理解基准**：构建504道多选题，涵盖拉格语法、文化知识、符号推理三个子任务，基于印度斯坦古典理论和孟加拉古典形式（如Rabindra Sangeet、Nazrul Sangeet）。手动整理100首参考乐谱（ABC符号）。
2. **5级受控提示框架**：逐步引入音阶、节奏、体裁、风格等约束，评估符号音乐生成能力。
3. **大规模评估**：在33个LLMs上进行理解评估（其中9个进行生成评估），同时采用自动结构指标和人工判断。

## 实验结果
- **理解任务**：前沿模型Gemini 2.5 Pro达85-90%准确率，开源模型仅23-40%。
- **生成任务**：最强模型在风格忠实度上仅40%合格；结构有效性（如正确音符）与风格忠实度（如装饰音）存在显著差距。自动指标无法捕捉文化特异性。

## 一句话评价
该工作首次系统评估LLMs在南亚古典音乐上的能力，揭示了结构有效性与风格忠实性是分离的目标，并验证了现有自动指标不足以评估文化引导的音乐生成。

---

## 29. nnAudio 2: Overcoming Dynamic Compilation Barriers and Transform Inconsistencies

**作者**: Abhinaba Roy, Junyi Liang, Dorien Herremans
**链接**: [2606.05394](https://arxiv.org/abs/2606.05394)
**分类**: Audio Feature Extraction | **关键词**: nnAudio, TorchScript, STFT, iSTFT, CQT, VQT, CFP, Differentiable audio front-end, Inverse transform, Landweber iteration

## 核心痛点
- nnAudio工具箱在现代化PyTorch环境中存在三个主要问题：
  1. TorchScript不兼容（STFT/iSTFT的延迟状态突变、动态子模块构造、可选参数类型不精确）导致无法部署。
  2. 逆STFT在非均匀频率尺度（freq_scale != 'no'）下静默返回错误波形，无错误提示。
  3. 依赖漂移：CFP因SciPy窗口函数重组织而失败，VQT在γ=0时未退化为CQT。

## 方法创新
作者提出5项保守但关键的现代化修复：
- **TorchScript兼容**：移除脚本化路径中的动态状态突变和子模块构造，为逆辅助函数提供精确静态类型。
- **逆STFT约束**：限制可靠逆变换仅适用于均匀频率尺度（freq_scale='no'），对其他尺度抛出显式运行时错误。
- **CFP修复**：将Blackman-Harris窗口导入从`scipy.signal`改为`scipy.signal.windows`。
- **VQT一致性**：确保γ=0时VQT退化为CQT，符合数学定义。
- **引入iCQT**：基于Landweber迭代的可微逆CQT模块，重建波形SNR>30 dB，支持端到端梯度传播。

## 实验结果
- 通过回归测试验证新的STFT/iSTFT行为。
- 完整仓库测试套件在最新Python/PyTorch环境下全部通过。
- TorchScript编译烟雾测试确认正向和逆向STFT可成功编译执行。
- iCQT在多个信号上实现>30 dB的重建SNR。

## 一句话评价
本文对nnAudio进行了工程导向的保守现代化，解决了阻碍研究和部署的关键兼容性与正确性问题，但未引入新算法或改进性能。

---

## 30. Task-Vector Arithmetic for Emotional Expressivity Control in Language-Model-Based Text-to-Speech

**作者**: Daniel Oliveira de Brito, Arnaldo Candido Junior
**链接**: [2606.05367](https://arxiv.org/abs/2606.05367)
**分类**: Text-to-Speech | **关键词**: task-vector arithmetic, emotional text-to-speech, x-vector, cross-speaker style transfer, language-model TTS

## 核心痛点
基于语言模型的文本转语音（LM-TTS）系统中，情感韵律的跨说话人控制面临挑战：传统任务向量算术在模块化架构中有效，但在LM-TTS中因架构差异（情感信息缺乏明确的权重功能位点）而失效。

## 方法创新
1. **消融研究**：通过四个逐步缩小的操作数（LoRA微调的模型权重、连续码本嵌入、离散码本令牌、x-向量）定位情感韵律的主要载体为ECAPA-TDNN编码器产生的x-向量。
2. **无训练跨说话人情感控制**：提出基于质心算术的方法，计算情感x-向量差τ_emo，应用于目标说话人以实现情感迁移，强度由α控制。
3. **跨语言验证**：在英语ESD上提取τ，应用于葡萄牙语emoUERJ数据集，验证跨语言泛化性。

## 实验结果
- 英语保留说话人：平均emotion2vec余弦比基线（ICL）提高+0.29；
- 巴西葡萄牙语保留说话人：提高+0.09；
- 说话人身份保持良好（WavLM SECS ≥ 0.88）；
- 葡萄牙语词错误率（WER）≈0。

## 一句话评价
该工作首次证明在LM-TTS中，基于说话人嵌入的质心算术可实现有效的无训练情感控制，且跨语言适用。

---

## 31. MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models

**作者**: Manh Luong, Tamas Abraham, Junae Kim, Amar Kaur, Rollin Omari, Gholamreza Haffari, Trang Vu, Lizhen Qu, Dinh Phung
**链接**: [2606.05177](https://arxiv.org/abs/2606.05177)
**分类**: Multimodal Safety Benchmark | **关键词**: Omni LLMs, safety assessment, multimodal benchmark, cross-modal reasoning, multicontext safety

## 核心痛点
当前多模态安全基准仅关注视觉模态，无法评估同时处理视觉、音频和文本的全能大语言模型（Omni LLMs）的安全性。现有基准依赖单一模态，不能反映现实世界中需要跨模态综合判断的复杂安全场景。

## 方法创新
- **MCBench基准**：首次提出多模态、多上下文安全基准，包含1196个场景，覆盖物理伤害、社会伤害、非法伤害和财产损失四大类。每个不安全场景配有一个仅最小上下文元素不同的安全场景，用于评估模型过度敏感/不敏感问题。
- **数据生成**：两阶段框架。阶段1利用Claude-Sonnet-4.5生成细粒度分类和If-Then逻辑的安全场景，经人工验证。阶段2用Gemini-Flash-2.5生成图像，Stable Audio 1.0生成音频，并处理敏感内容过滤。
- **评估维度**：不仅评估安全分类准确性，还通过谓词分析模型跨模态推理能力。

## 实验结果
- 当前Omni LLMs在社会伤害和非法伤害等微妙/非物理风险场景表现差，在物理伤害和财产损失等有显著视觉/听觉线索的场景表现较好。
- 模型能正确提取单模态信息，但缺乏有效的跨模态整合能力，导致安全判断失败。
- 模型存在过度敏感问题，面对模糊线索时仅关注单一可疑信号而忽略其他模态矛盾证据，导致安全场景的假阳性。

## 一句话评价
MCBench揭示了当前Omni LLMs在跨模态安全推理上的严重缺陷，为提升多模态模型的安全感知能力提供了关键基准和诊断工具。

---

