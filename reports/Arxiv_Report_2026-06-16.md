# Arxiv Daily Deep Report - 2026-06-16

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 36
---

## 1. CraBERT: Efficient Phoneme Encoder Pre-Training via Cascade Fusion of Subword Representations for Text-to-Speech

**作者**: Dong Yang, Yuki Saito, Wataru Nakata, Hiroshi Saruwatari
**链接**: [2606.16668](https://arxiv.org/abs/2606.16668)
**分类**: Text-to-Speech | **关键词**: 预训练音素编码器, 级联融合, 子词-音素对齐, 动态时间规整, BERT, Text-to-Speech

## 核心痛点
现有预训练音素编码器（PPEnc）如 MP BERT、PL BERT 需要大量预训练（约10个epoch）才能获得较好性能，主要原因是音素序列长、词汇量小、语义编码困难，导致学习词级和句级特征效率低。

## 方法创新
提出 **CraBERT**，采用级联融合架构：
1. 使用冻结的预训练子词级 DistilBERT 提供词/句级先验信息；
2. 通过基于动态时间规整（DTW）的子词-音素对齐算法，将子词表示上采样后与音素嵌入逐元素相加，再输入音素级 BERT（PBERT）；
3. 预训练任务包括掩码语言建模（MLM）和音素到词（P2G）预测，权重共享与初始化加速收敛。

## 实验结果
- 仅预训练约1个epoch，CraBERT 的 MOS 值与预训练约10个epoch的 MP BERT、PL BERT 相当。
- 高掩码率（>15%）在该高效策略下更优。

## 一句话评价
CraBERT 通过级联融合预训练子词表示，大幅降低了音素编码器的预训练成本，同时在语音合成自然度和韵律上保持竞争力。

---

## 2. Learning Input-Channel Permutation Equivariance for Multi-Channel Source Separation: Reducing Bleeding in Small Music Ensembles

**作者**: Ruchi Pandey, Jaime Garcia-Martinez, Pablo Cabanas-Molero, David Diaz Guerra, Ricardo Falcon Perez, Tuomas Virtanen, Julio J. Carabias-Orti, Pedro Vera-Candeas
**链接**: [2606.16551](https://arxiv.org/abs/2606.16551)
**分类**: 音频源分离 / 音乐源分离 (Audio Source Separation / Music Source Separation) | **关键词**: Microphone bleed, Music source separation, Permutation equivariance, Deep learning, Hybrid Demucs, Multi-channel separation, Small ensembles

## 核心痛点
小型合奏或管弦乐录音中，近距离麦克风会捕获相邻声源的泄漏（bleeding），导致音轨隔离困难，影响混音质量。

## 方法创新
本文提出将**通道排列等变性**作为核心学习原则：训练时对输入麦克风通道和对应的参考目标施加相同的随机排列，迫使模型学习排列等变的映射，减少对固定通道-乐器关联的依赖，从而提升对录音设置变化的鲁棒性。在Hybrid Demucs架构基础上改编为多通道版本，输入P路近场麦克风信号，输出P路去串扰估计。

## 实验结果
在合成数据（SynthSOD弦乐合奏）和真实URMP录音上评估，使用SDR作为指标。与不采用排列训练（No perm）的基线相比，排列感知训练（Perm）在未见过的房间、布局和真实录音上均显著改善SDR（如URMP弦乐合奏平均SDR提升从+0.3 dB增至+5.3 dB（幅度谱输入））。

## 一句话评价
本文提出了一种简洁有效的数据驱动策略——通道排列等变性训练，显著提升了多通道音乐源分离在去串扰任务中的泛化能力。

---

## 3. Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition

**作者**: Chengxi Deng, Xurong Xie, Shujie Hu, Jiajun Deng, Mengzhe Geng, Youjun Chen, Huimeng Wang, Haoning Xu, Guinan Li, Xunying Liu
**链接**: [2606.16546](https://arxiv.org/abs/2606.16546)
**分类**: Speech Recognition | **关键词**: Semi-supervised Learning, Pseudo-labeling, Confidence Estimation, Speaker Adaptation, Elderly Speech Recognition, Whisper

## 核心痛点
老年人语音识别面临三大挑战：1) 标注数据稀缺且成本高昂；2) 伪标签质量不可靠，直接解码错误率高；3) 说话人间异质性（发音退化、语言退化等）加剧了系统性能下降。

## 方法创新
提出一种结合**置信度分数引导的增量式伪标签**与**说话人自适应训练**的半监督方法：
1. **置信度估计模块（CEM）**：轻量级二元分类器（3层残差FFN），基于Whisper解码输出和top-10 logits逐令牌预测置信度，通过编辑距离对齐训练，并对无标签数据取平均得到语句级分数。
2. **置信度引导的数据排序**：对每位说话人内语句按置信度降序排列，均分为K组，跨说话人组合形成从高到低置信度的K个子集。
3. **增量式伪标签**：按照课程学习轨迹，从高置信度子集开始逐步加入训练。每次迭代用当前模型为下一子集重新生成伪标签，并合并所有已处理子集进行微调。
4. **说话人自适应训练**：为每位训练说话人初始化可学习说话人提示（prompt），与输入拼接，通过LoRA联合训练说话人提示和适应参数，解码时采用说话人自适应模型提升伪标签质量。

## 实验结果
在**DementiaBank Pitt**（英语）和**JCCOCC MoCA**（粤语）老年人语音数据集上，相比半监督基线方法，词错误率（WER）或字符错误率（CER）绝对降低1.45%和2.27%（相对降低6.21%和6.98%），差异具有统计显著性。

## 一句话评价
首次将置信度引导的增量伪标签与说话人自适应训练结合，有效缓解了老年人语音半监督学习中的标签噪声和异质性挑战。

---

## 4. Decoding while Adapting: Zero-Shot Online Speaker Adaptation via Audio-Textual Prompts for Elderly Speech Recognition

**作者**: Chengxi Deng, Xurong Xie, Shujie Hu, Mengzhe Geng, Tianzi Wang, Youjun Chen, Huimeng Wang, Haoning Xu, Jiajun Deng, Xunying Liu
**链接**: [2606.16539](https://arxiv.org/abs/2606.16539)
**分类**: Speech Recognition | **关键词**: Elderly Speech Recognition, Zero-Shot Speaker Adaptation, Online Adaptation, Audio-Textual Prompts, Cross-Modality Fusion, Whisper, Q-Former

## 核心痛点
老年人语音识别面临多重挑战：说话人异质性、数据稀疏、言语产生和语言能力衰退、缺乏跨语句上下文信息。现有说话人自适应方法存在延迟高、未有效融合音频和文本信息、缺乏跨语句文本信息等局限。

## 方法创新
提出一种基于跨语句音频-文本提示的在线说话人自适应方法，用于老年人语音识别。该方法通过双跨模态融合（Dual Cross-Modality Fusion）整合历史语音和文本信息，利用Q-Former模块压缩可变长度的历史上下文，生成紧凑的说话人提示（speaker prompts），实现零样本、实时的自适应。训练分为两步：说话人自适应训练（SAT）和在线音频-文本提示自适应。测试时，系统能同时解码和自适应（"decoding while adapting"），无需伪标签或额外延迟。

## 实验结果
在英语DementiaBank Pitt和粤语JCCOCC MoCA老年人语音数据集上，所提在线自适应方法相比说话人无关（SI）模型显著降低了词错误率（WER）或字符错误率（CER），分别绝对降低0.61%和1.22%（相对降低2.99%和4.48%）。实时因子（RTF）加速比高达9.83倍，优于离线批处理自适应。与i-vector、x-vector、ECAPA-TDNN等基线相比，音频-文本提示方法表现更优。

## 一句话评价
该工作首次将跨语句音频-文本提示用于老年人语音识别的在线说话人自适应，实现了低延迟、高性能的零样本自适应。

---

## 5. Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec

**作者**: Haixin Zhao, Nilesh Madhu
**链接**: [2606.16464](https://arxiv.org/abs/2606.16464)
**分类**: Speech Enhancement | **关键词**: speech enhancement, vector quantisation, neural audio codec, regularisation, generative model, continuous latent space, discrete latent space

### 核心痛点
现有基于向量量化（VQ）的神经音频编解码器（NAC）语音增强方法，在离散和连续潜空间中的建模策略差异未被充分探索，且VQ正则化的内在作用（独立于离散处理）未被分离验证。此外，预训练编解码器在噪声输入下的匹配问题导致性能下降。

### 方法创新
1. **提出两种框架**：
   - **cNAC-SE**：在连续潜空间预测清洁表示，并在增强后引入VQ模块作为清洁先验正则化。
   - **dNAC-SE**：先对潜表示进行残差VQ离散化，再通过基于transformer的增强器预测离散token（码本索引）。
2. **探索三种离散建模策略**：独立建模（IM）、联合建模（JM）、混合建模（HM），处理残差级embedding的依赖关系。
3. **全微调策略**：对编解码器进行微调（dNAC-SE采用分阶段硬/软微调），提升泛化能力。
4. **理论分析**：通过潜空间可视化和PCA实验，揭示cNAC-SE预测偏差集中在清洁先验附近，而dNAC-SE离散分类导致离散分布且存在显著漂移。

### 实验结果
- 全微调cNAC-SE在所有测试条件下一致优于所有dNAC-SE变体（IM/JM/HM），并在DNS-MOS指标上达到生成方法中的领先水平。
- 对比判别式变体（无VQ正则化），VQ通过清洁先验约束正则化显著提升鲁棒性，证明其价值可迁移至连续建模。
- 编解码器微调带来显著性能提升，尤其对cNAC-SE。

### 一句话评价
本文通过系统比较连续与离散潜空间建模，揭示了VQ正则化对鲁棒性的内在贡献，并提出了基于连续潜空间预测且结合VQ正则化的高性能生成式语音增强框架cNAC-SE。

---

## 6. Unified Audio Generation and Editing via Joint Condition Modeling and Progressive Training

**作者**: Haocheng Dong, Yuheng Lu, Cheng Gong, Shansong Liu, Xiao-Lei Zhang, Xuelong Li
**链接**: [2606.16435](https://arxiv.org/abs/2606.16435)
**分类**: Audio Generation | **关键词**: 统一音频生成, 音频编辑, 扩散Transformer, 流匹配, 联合条件建模, 渐进训练

## 核心痛点
现有方法通常将文本到音频生成（TTA）和音频编辑视为独立任务，采用任务特定的架构或模块，导致系统复杂、可扩展性差，且忽视了任务间交互的潜在益处。

## 方法创新
提出 **AudioWeave** 统一模型：
1. **联合条件建模**：通过因子化位置嵌入，使单个扩散Transformer（DiT）骨干能同时处理TTA和音频编辑的异构输入条件（文本、参考音频）。
2. **渐进多阶段训练策略**：先预训练TTA基础模型，再混合训练TTA和音频编辑，结合任务特定注意力掩码，缓解任务竞争和灾难性遗忘。
3. 采用流匹配（Flow Matching）目标训练，结合混合DiT架构（双流MMDiT块和单流DiT块）。

## 实验结果
在TTA和六个音频编辑任务上，统一模型达到了与任务特定模型相当的性能，验证了方法的有效性。

## 一句话评价
AudioWeave通过联合条件建模和渐进训练，首次实现了无需任务特定组件的统一音频生成与编辑，为多任务音频生成奠定了基础。

---

## 7. Stabilizing Short Duration Speaker Verification through Neural Re-scoring with Hybrid Enrollment

**作者**: Zhiqi Ai, Han Cheng, Shiyi Mu, Zhiyong Chen, Yongjin Zhou, Shugong Xu
**链接**: [2606.16115](https://arxiv.org/abs/2606.16115)
**分类**: Speaker Verification | **关键词**: short-duration speaker verification, hybrid enrollment, neural re-scoring, VoxPhrase, text-dependent, text-independent, parallel cross-attention

## 核心痛点
短时说话人验证（SDSV）中，测试语音通常短于3秒，导致说话人表示不稳定，对噪声和音素变化敏感，性能下降。

## 方法创新
1. **VoxPhrase数据集**：从VoxCeleb自动分割的大规模SDSV语料库，支持定制化短语注册。
2. **混合注册策略**：结合文本相关（TD）和文本无关（TI）注册，TD保证内容一致性但受时长限制，TI提供更丰富且稳定的表示但存在内容不匹配。
3. **神经重评分框架**：通过冻结的说话人主干提取帧级和话语级特征，采用并行交叉注意力进行帧级匹配，并融合全局相似度，最终经MLP输出验证分数。

## 实验结果
- 在所测试的时长范围内（TI 3s/10s vs TD 0.8-3s），TI注册优于TD。
- 引入神经验证器后，TD场景下一致提升（EER从3.62%降至3.09%）。
- 混合注册+神经重评分在多种主干模型（ECAPA-TDNN, CAM++, ERes2Net-L）上均取得显著改进，尤其在困难样本场景下鲁棒性突出。

## 一句话评价
提出混合注册与帧级神经重评分结合的方法，有效解决了短时说话人验证中的表示不稳定问题，并在大规模数据集上验证了有效性。

---

## 8. Bridging the SEA Gap: An Initial Benchmark for Neural Audio Codec-Synthesized Speech Deepfakes in South-East Asian Languages

**作者**: Orchid Chetia Phukan, Girish, Mohd Mujtaba Akhtar, Arun Balaji Buduru
**链接**: [2606.15968](https://arxiv.org/abs/2606.15968)
**分类**: Speech Deepfake Detection | **关键词**: Codecfakes, Neural Audio Codec, South-East Asian languages, Deepfake detection, Audio Language Model, Lightweight model, GARUDA, SEA-CF

## 核心痛点
现有Codecfake（CF）检测基准主要集中于英语（少量中文），忽略了东南亚（SEA）语言。SEA语言具有独特的语音、声调及韵律结构，导致英语训练的检测器泛化性差。此外，现有音频语言模型（ALM）体积庞大，不适合低资源、低延迟场景。

## 方法创新
1. **SEA-CF数据集**：首个大规模SEA语言CF检测基准，涵盖泰米尔语、印地语、泰语、印尼语、马来语、越南语，使用多种神经音频编解码器（NAC）合成。
2. **GARUDA小型ALM**：专为CF检测设计的轻量级音频语言模型（<1B参数），推理时间仅1.21秒，兼顾性能与效率。
3. **零样本与微调评估**：系统评估了现有SOTA ALM在SEA-CF上的表现，并验证了GARUDA的优越性。

## 实验结果
- 英语训练的CF检测器在SEA-CF上表现差，联合训练（SEA-CF + 现有CF基准）可提升性能，表明领域内训练的必要性。
- GARUDA在SEA-CF及现有CF基准上均达到SOTA，且轻量高效，适用于实时检测场景。

## 一句话评价
该工作填补了SEA语言CF检测的空白，并提供了实用化的轻量级解决方案。

---

## 9. Geometrically Constrained Decentralized Independent Vector Analysis for Distributed Microphone Arrays

**作者**: Changda Chen, Yichen Yang, Wei Liu, Bing Zhu, Gongping Huang, Shoji Makino, Shuai Wang
**链接**: [2606.15826](https://arxiv.org/abs/2606.15826)
**分类**: Blind Source Separation | **关键词**: blind source separation, independent vector analysis, distributed microphone arrays, direction of arrival, geometric constraint

## 核心痛点
传统的 Dec-IVA 方法在分布式麦克风阵列中，由于不同阵列间的输出排列不一致（permutation inconsistency）以及源模型假设的强跨阵列依赖，导致分离性能提升有限，甚至不如局部 IVA。

## 方法创新
1. **几何约束（GC）**：引入 DOA 信息作为先验，通过在 MAP 框架下对解混矩阵施加几何约束，强制不同阵列的同一输出索引对应同一说话人，解决排列不一致问题。
2. **新源模型**：将原全局源活动度量（按所有频点求功率和）改为每个阵列内部独立计算，再求和，以削弱跨阵列依赖，提高对排列不一致的鲁棒性。
3. **优化算法**：基于 VCD 迭代更新辅助变量和解混矩阵，推导出带约束的闭式更新公式。

## 实验结果
- 在模拟混响房间中，使用 2 到 8 个双麦克风阵列，无噪声和有噪声条件下，GC-Dec-IVA 相比 Loc-IVA 和 Dec-IVA 均显著提升分离性能（SDR）和跨阵列排列一致性。
- 在真实环境录音中也验证了有效性。

## 一句话评价
首次将 DOA 几何约束引入分布式 IVA，通过约束排列和弱化跨阵列依赖，实现了更鲁棒、更高效的分布式盲源分离。

---

## 10. AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control

**作者**: Dabin Kim, Junwon Lee, Juhan Nam
**链接**: [2606.15813](https://arxiv.org/abs/2606.15813)
**分类**: Audio Generation / Music Editing | **关键词**: timbre transfer, text-to-music, ControlNet, diffusion transformer, target-adaptive scaling

## 核心痛点
细粒度音色迁移中，源乐器的乐器特有表现细节（如颤音、起音）与目标乐器不兼容，导致音色模糊和伪影。现有方法（如ControlNet微调）会刚性保留所有细节，损害目标音色真实性。

## 方法创新
提出**AdaTT**：一种目标自适应机制，在ControlNet框架内通过文本提示动态缩放音高和响度控制信号的帧级影响。包含两个关键模块：
- **Control Scale Predictors (CSPs)**：对ControlNet输出进行帧级缩放。
- **Text-Guided CSPs (TG-CSPs)**：结合文本嵌入独立调节音高和响度控制输入，实现信号级调制。
此外，设计**半自动数据构建流水线**，利用SAO-ControlNet推理和专家验证生成跨乐器配对训练数据。

## 实验结果
在URMP和Solos数据集上，AdaTT在CLAP分数（音色保真度）和Chroma分数（结构一致性）上均优于基线（SAO-ControlNet），尤其在跨乐器迁移中表现更佳。音频示例见项目页面。

## 一句话评价
AdaTT通过目标自适应控制平衡结构保持与音色真实性，是细粒度音色迁移的有效方案。

---

## 11. MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio

**作者**: Salman Hussain Ali, Umberto Cappellazzo, Mirco Ravanelli
**链接**: [2606.15638](https://arxiv.org/abs/2606.15638)
**分类**: Parameter-Efficient Transfer Learning for Speech and Audio | **关键词**: Mamba, Parameter-Efficient Transfer Learning, Speech Recognition, Audio Classification, State-Space Models, Adapters

# MambAdapter: 基于Mamba的轻量级适配器用于语音和音频参数高效迁移学习

## 核心痛点
微调大规模Transformer基础模型（如Whisper、AST）在语音和音频任务中计算和内存成本高昂。现有参数高效迁移学习(PETL)方法（如Bottleneck适配器、LoRA、Conformer适配器）虽然降低了参数量，但性能仍有提升空间，且未能利用新兴的状态空间模型Mamba的优势。

## 方法创新
- **MambAdapter架构**：将Mamba模块集成到低秩瓶颈适配器中，结合共享线性投影（跨层共享W_down和W_up）和可学习缩放因子α，在低秩潜在空间中利用Mamba的长程时序建模能力。
- **参数共享**：通过共享投影矩阵，减少线性投影的参数成本（从2drl降至2dr），同时Mamba模块提供层特定建模能力，实现高效参数利用。
- **理论依据**：状态空间模型将时序信息压缩到低维潜状态（N≪d），与低秩适配器（r≪d）自然匹配，表明Mamba适合参数高效迁移学习。

## 实验结果
- **音频/语音分类**（AST模型）：在ESC-50、UrbanSound8K、Speech Commands V2、Fluent Speech Commands四个数据集上，MambAdapter在使用不到25%参数的情况下，平均准确率接近或超过Conformer适配器（Pfeiffer配置：89.72% vs 90.07%；Houlsby配置：89.85% vs 89.69%）。
- **多语言语音识别**（Whisper模型）：在Abkhaz、Central Kurdish等五种语言上，MambAdapter取得平均WER 49.9%，优于LoRA（57.3%）、Bottleneck（50.7%）、Conformer（55.7%），且参数最少（1.1M vs FFT的241M）。
- **参数效率**：在更少参数下匹配或超越强基线，验证了Mamba在PETL中的有效性。

## 一句话评价
这是首次将Mamba状态空间模型作为参数高效迁移学习技术应用于语音和音频，通过轻量级共享投影和低秩Mamba块，在显著减少参数的同时，实现了可比或更优的性能。

---

## 12. Phonetically Explainable Speech Deepfake Detection

**作者**: Manasi Chhibber, Jagabandhu Mishra, Tomi H. Kinnunen
**链接**: [2606.15454](https://arxiv.org/abs/2606.15454)
**分类**: Speech Anti-spoofing / Deepfake Detection | **关键词**: Cross-attention, Phonetics, Speech Deepfakes, Anti-spoofing, Interpretability, Explainable AI

## 核心痛点
现有语音深度伪造检测方法通常将整个话语作为黑盒处理，通过时间平均或注意力机制聚合声学特征，忽视了不同音素类别携带的信息量差异，导致决策缺乏可解释性。

## 方法创新
提出音素引导的交叉注意力框架，将检测分解为可解释的音素条件过程：基于三个概率假设（音素估计充分性、声学主导音素估计误差、音素先验无信息），将欺骗后验概率因子化为音素类别出现权重与类条件欺骗概率的加权和。架构使用自监督声学流（XLS-R）和音素后验概率图（PPG）交叉注意力，音素锚点作为查询，声学特征作为键值，输出显式的每音素权重，实现结构化的可解释性。

## 实验结果
在三个数据集（LJSpeech衍生、ASVspoof 2019 LA、ASVspoof 5 Track 1）上验证，发现塞音、擦音、塞擦音、鼻音和静默边界闭锁具有最高判别力，而元音和半元音重要性较低。通过音素组消融实验证实了这一排序。

## 一句话评价
首次将音素级可解释性内置到深度伪造检测架构中，通过概率因子化和交叉注意力实现透明决策，兼顾性能与解释性。

---

## 13. DDPO-VC: Speaker De-Identification via Diffusion Denoising Policy Optimization

**作者**: Liming Wang, Cody Karjadi, Rhoda Au, James Glass
**链接**: [2606.15313](https://arxiv.org/abs/2606.15313)
**分类**: Speaker De-identification / Voice Conversion | **关键词**: speaker de-identification, speaker anonymization, voice conversion, diffusion models, reinforcement learning, privacy-utility tradeoff, dementia speech

# 论文总结

## 核心痛点
说话人去识别（Speaker De-identification）的关键挑战在于平衡隐私保护（移除说话人身份信息）与下游任务效用（如认知健康检测）之间的冲突。传统基于解耦（disentanglement）的方法假设隐私变量（说话人身份）与效用变量（如痴呆症状态）独立，但在健康领域这些变量常常相关，导致隐私泄露或效用损失。

## 方法创新
提出 **DDPO-VC** 框架，通过强化学习（RL）后训练扩散模型（Diffusion Model）实现说话人去识别。主要创新点：
1. 使用**扩散模型**进行语音生成，避免量化损失，提升自然度。
2. 引入**强化学习**（DDPO）通过奖励信号优化隐私-效用权衡，无需对潜在变量做显式建模。
3. 结合**隐私教师**（说话人验证器）和**效用教师**（痴呆症分类器）设计奖励函数。
4. 采用归一化奖励和信任区域约束稳定训练。

## 实验结果
在两个痴呆症语音基准（ADReSS 和 FHS）上，DDPO-VC 在隐私保护（EER）和认知效用（AUC）方面均优于多种强基线方法。

## 一句话评价
提出了一种新颖的基于 RL 后训练扩散模型的说话人去识别框架，有效处理隐私-效用相关场景，尤其在健康领域表现出色。

---

## 14. Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity

**作者**: Zhenwei Mou, Liping Chen, Yajun Hu, Zhen-Hua Ling, Xin Fang, Jianqing Gao
**链接**: [2606.15267](https://arxiv.org/abs/2606.15267)
**分类**: Text-to-Speech | **关键词**: LLM-based TTS, speaker similarity, speaking style, dynamic prosody prediction

# 总结

## 核心痛点
当前基于LLM的TTS方法（如CosyVoice）缺乏对说话风格中韵律模式的显式建模，导致合成语音的说话人相似性受限。已有方法（如CoT prompting）静态预计算整个话语的韵律，忽略了目标语音的特定风格。

## 方法创新
提出动态韵律预测方法：在生成每个音节的语音帧之前，基于目标文本、参考语音以及先前已预测的语音，动态预测当前音节的韵律。韵律由音节级特征（时长、平均能量、平均音高、音高范围）经k-means聚类得到韵律token。整体架构基于CosyVoice，LLM交替生成韵律token和语音token，并利用先前生成的韵律和语音token作为条件。

## 实验结果
在中文数据集（ESD、内部、AISHELL-3）上进行了MOS和偏好测试。与CosyVoice(50k)和CoT方法相比，所提方法在MOS上略有提升或持平，但在偏好测试中表现出更高的说话人相似性（ESD上偏好达51.5%）。此外，动态韵律预测方法在小规模训练数据上展现出缩小韵律学习差距的潜力。

## 一句话评价
动态韵律预测通过将先前预测语音融入韵律建模，有效增强了LLM-based TTS的说话人相似性。

---

## 15. DuraMark: Duration-Embedded Watermarking in LLM-based TTS

**作者**: Zhenwei Mou, Weili Jiang, Liping Chen, Zhen-Hua Ling, Kong Aik Lee, Kai Gao, Boyu Zhao
**链接**: [2606.15264](https://arxiv.org/abs/2606.15264)
**分类**: Text-to-Speech | **关键词**: speech watermarking, duration-embedded watermarking, robustness, duration-controllable LLM-based TTS

## 论文总结

**DuraMark: Duration-Embedded Watermarking in LLM-based TTS**

### 核心痛点
- LLM-based TTS 的语音克隆能力引发深度伪造滥用风险。
- 现有信号级水印（波形或频谱图）易受生成式攻击（如神经编解码器、声码器）破坏，鲁棒性不足。
- 信息级方法（如修改音高）导致韵律不自然。

### 方法创新
- 提出 **DuraMark**，一种基于音节时长编辑的信息级水印框架，工作于 LLM-based TTS 系统。
- 开发了 **时长可控的 LLM-based TTS 模型**（含 LLM 预测时长和语音 token、流匹配解码器），可在合成时精确编辑音节时长。
- 设计 **时长提取器**，从语音中提取音节时长序列用于检测。
- 水印嵌入：通过将原始时长编辑为偶数（比特 0）或奇数（比特 1）来编码水印信息。
- 检测：计算提取的时长序列与水印序列的相似度，与阈值比较判断水印是否存在。

### 实验结果
- 在中文数据集（WenetSpeech 训练，AISHELL-3 测试）上，DuraMark 在生成式攻击（神经编解码器、声码器如 HiFi-GAN、Encodec、SoundStream）下显著优于信号级基线（AudioSeal、WavMark 等），TPR 更高。
- 语音长度增加时，检测性能提升（如 DuraMark-Info 在 17-32 音节时 TPR=0.981，65-100 音节时 TPR=0.998）。
- 支持盲检测（无需原始语音）和带辅助信息（有原始语音）两种检测模式。

### 一句话评价
DuraMark 通过创新的时长级水印嵌入范式，在保证语音质量的同时，大幅提升了对抗生成式攻击的鲁棒性，为 LLM-based TTS 的版权保护和溯源提供了新方案。

---

## 16. VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations

**作者**: Farnaz Sedaghati, Yuxi Wang, Zicheng Weng, Wei Rao
**链接**: [2606.15187](https://arxiv.org/abs/2606.15187)
**分类**: Audio Watermarking & Detection | **关键词**: audio watermarking, watermark detection, benchmark dataset, black-box attack, robustness evaluation

## 核心痛点
现有音频水印检测研究缺乏统一的大规模基准，无法系统比较不同水印注入方法在真实分布偏移（如压缩、噪声、对抗攻击）下的检测性能。

## 方法创新
1. **VoxWatermark基准**：首个面向音频水印检测的大规模基准，涵盖25种语言、126,513.89小时音频，包含干净、水印及扰动样本。
2. **扰动协议**：提出no-box（17种信号处理）、black-box（HSJ、Square Attack）、white-box（梯度优化）三类扰动，模拟真实传输与攻击场景。
3. **AudioWMD检测器**：两阶段流水线（基检测器+查询统计元分类），统一基线，跨语料库与分布鲁棒。
4. **水印方法覆盖**：10种方法（4种神经网络：AudioSeal、WavMark、Timbre、Perth；6种传统：LSB、QIM、Patchwork、Echo Hiding、Phase Coding、DSSS），统一注入与标注。

## 实验结果（基于摘要）
- 注入方法多样性和分布偏移显著影响检测稳定性。
- AudioWMD在跨语料库与跨扰动设置下验证了有效性与可扩展性。

## 一句话评价
VoxWatermark填补了音频水印检测缺乏统一基准的空白，为鲁棒检测研究提供了标准化平台。

---

## 17. EChO-Agent: Evidence Chain Orchestration Agent for Audio Reasoning

**作者**: Siyuan Zhang, Jian Zong, Junyu Wang, Peiyuan Jiang, Jiahao Yan, Jingyu Zhang, Tianrui Wang, Xiaobao Wang, Longbiao Wang, Jianwu Dang
**链接**: [2606.15141](https://arxiv.org/abs/2606.15141)
**分类**: Audio Reasoning | **关键词**: audio reasoning, tool-augmented agent, large audio language model, chain-of-thought verification, evidence chain

## 核心痛点
当前大型音频语言模型（LALM）在复杂音频推理任务中存在以下问题：
- 缺乏问题条件化的感知，无法聚焦于与问题相关的音频片段；
- 推理链不可检查，难以验证其真实性；
- 缺少领域知识且无法重新访问音频以恢复遗漏信号；
- 评估不仅关注答案正确性，还需推理过程忠实于音频证据（如Interspeech 2026音频推理挑战赛的rubric评分）。

## 方法创新
提出**EChO-Agent**，一种模块化智能体框架，将复杂音频问答分解为四阶段流水线：
1. **工具增强观察**：根据问题类型静态调度预定义工具（音频事件检测、ASR、语音情感识别、音乐分析），生成原始观测。
2. **LLM证据整合**：使用DeepSeek-V3进行相关性过滤、跨观测合成和证据结构化，将原始观测转化为紧凑、问题导向的证据链。
3. **证据条件音频推理**：以Qwen-3-Omni-Instruct为骨干，结合原始音频、问题和结构化证据，生成逐步推理的候选答案。
4. **验证与输出仲裁**：进行格式合规性检查、推理-答案一致性检查，并通过双通道仲裁从两个候选答案中选择最终输出。

关键创新点在于将工具输出转化为结构化证据，并强制推理过程基于证据，同时引入自我验证机制。

## 实验结果
- 在MMAR基准上，EChO-Agent达到**71.0%准确率**和**63.0 rubric分数**，相比Qwen-3-Omni基线分别提升+2.3和+4.3，在MMAR智能体赛道排名第5。
- 消融实验证实：**证据整合是关键因素**，移除后性能下降最大，甚至低于无工具基线；验证阶段减少可避免的最后一英里错误。
- 在多模态混合场景（如声音-音乐-语音）中表现尤为突出（75.0%准确率）。

## 一句话评价
EChO-Agent通过结构化证据链和自验证机制显著提升了音频推理的准确性和推理过程的可信度，为解决LALM在复杂音频推理中的局限性提供了有效方案。

---

## 18. From Physics to Representation: Audio Learning with Synthetic Pre-training via Procedural Generation

**作者**: Fengrui Liu, Ruiyang Huang, Qijian Zheng, Yuanfang Wang, Feng Liu
**链接**: [2606.14791](https://arxiv.org/abs/2606.14791)
**分类**: Audio Self-Supervised Learning | **关键词**: Procedural Audio Synthesis, Self-Supervised Learning, Masked Autoencoders, Sim-to-Real Transfer, Audio Representation Learning

## 核心痛点
当前自监督音频表示学习严重依赖大规模真实音频数据集（如AudioSet、LibriSpeech），带来高昂的数据收集、清洗和隐私成本，且学到的表示易受数据分布偏差影响，缺乏对音频生成因素的可解释性。

## 方法创新
提出AudioPG框架，完全摒弃真实数据，采用程序化音频合成器实时生成无限多样的音频课程。合成器基于物理声学原理，通过参数化基元（谐波合成、调频、宽带脉冲、ADSR包络、瞬态噪声、频谱阻尼等）组合生成波形。然后训练Transformer掩码自编码器（MAE）在log-Mel频谱图上进行75%掩码重建，迫使模型学习音频的组成结构规律。预训练仅需单GPU 20分钟，无需任何真实录音。

## 实验结果
- ESC-50：90.60%准确率
- FSD50K：0.546 mAP
- UrbanSound8K：88.17%准确率
- Speech Commands V2：97.03%准确率
预训练效率比AudioMAE和SSAST快32倍（850 vs 50 epochs）。潜空间分析显示基频、相对强度等物理属性在正交子空间中自然解耦，可线性解码。

## 一句话评价
首次验证了无需真实数据的纯合成音频预训练可达顶尖迁移性能，兼具高效、可解释和强泛化能力。

---

## 19. Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech

**作者**: Adarsh Arigala, Arjun Gangwar, S Umesh, Yova Kementchedjhieva
**链接**: [2606.14750](https://arxiv.org/abs/2606.14750)
**分类**: Text-to-Speech | **关键词**: Pixel-TTS, Text-to-Speech, Pixel-Level Text Encoding, Cross-Lingual Speech Synthesis, Orthographic Noise Robustness

## 核心痛点
传统TTS系统依赖离散的Unicode嵌入，每个字符独立处理，导致对未见字符泛化能力差，跨语言适应时需扩展嵌入矩阵，增加模型复杂度和训练成本。

## 方法创新
提出Pixel-TTS，首个基于视觉文本表示的端到端TTS框架。将文本渲染为16×16灰度图像，通过2D卷积（核大小16×16，步长16×16）将每个patch映射为512维嵌入，利用ConvNeXtV2块处理。采用条件流匹配（CFM）损失，结合CTC文本对齐和HuBERT语音表示对齐的辅助损失。无需嵌入矩阵扩展，利用视觉相似性加速收敛。

## 实验结果
- **英语（LibriSpeech-PC）**：300k步后Pixel-TTS WER 2.28%（Text-TTS 2.53%），CER 0.81%（Text-TTS 1.16%），SIM和UTMOS相当。
- **零样本跨语言（德语、法语、荷兰语）**：Pixel-TTS在含OOV字符的测试集上错误率更低，鲁棒性更强。
- **低资源微调（德语10h/50h）**：Pixel-TTS无需扩展嵌入矩阵，WER和CER低于Text-TTS，收敛更快。
- **正字法噪声（Unicode同形符、l33tspeak）**：Pixel-TTS的WER和UTMOS退化更平缓，鲁棒性显著优于Text-TTS。

## 一句话评价
Pixel-TTS通过像素级文本编码有效提升了TTS在跨语言、低资源和噪声场景下的泛化能力，同时保持合成质量。

---

## 20. TuneJury: An Open Metric for Improving Music Generation Preference Alignment

**作者**: Yonghyun Kim, Junwon Lee, Haiwen Xia, Yinghao Ma, Junghyun Koo, Koichi Saito, Yuki Mitsufuji, Chris Donahue
**链接**: [2606.17006](https://arxiv.org/abs/2606.17006)
**分类**: Music Generation Evaluation / Text-to-Music Preference Alignment | **关键词**: Reward Model, Music Generation, Preference Alignment, Text-to-Music, Bradley-Terry, RankNet, Anchor Calibration

## 核心痛点
文本到音乐生成（TTM）的客观评估缺乏能够反映人类偏好的细粒度指标。现有指标如FAD衡量分布相似性而非人类偏好，且无法对单个生成进行评分。绝对MOS回归受评分者主观尺度漂移影响，而成对比较（A vs B）能更可靠地捕获偏好。

## 方法创新
**TuneJury** 是一个开源的、实例级别的成对奖励模型，输入为文本提示和音频片段，输出一个偏好分数。架构上，使用冻结的LAION-CLAP（文本+音频）和MERT（音频）编码器，拼接2048维嵌入，通过约2.8M参数的可训练MLP头得到标量分数。训练采用RankNet的共享权重成对逻辑损失，数据来自四个公开人类标注来源（Music Arena、MusicPrefs、AIME、SongEval），共约17.5K训练对，不使用伪标签增强。
此外，提出了**锚定校准（Anchor Calibration）**，一种事后、逐系统的Bradley-Terry校准方法，能够仅用约25倍少的校准数据匹配重新训练的精度，适应新TTM系统。

## 实验结果
- 在CMI-RewardBench上，TuneJury的成对准确率与作者间一致性相当（30对人工天花板测试）。
- 在PAM和MusicEval上，TuneJury的Spearman秩相关系数比不含伪标签的CMI-RM消融实验高0.17，且与全伪标签增强的CMI-RM在OOD分割上相差不到2个百分点。
- 三个下游应用（最佳N选择、DITTO风格潜在优化、专家迭代后训练）均显示一致的奖励轴增益。

## 一句话评价
TuneJury以极小的参数量和大规模的纯人工偏好数据，实现了具有竞争力的音乐生成偏好预测，并通过锚定校准实现高效的系统适应。

---

## 21. Probing Low Frame Rate Degradation in Neural Audio Codecs

**作者**: Alex Gichamba, Moise Busogi
**链接**: [2606.16969](https://arxiv.org/abs/2606.16969)
**分类**: Neural Audio Codec | **关键词**: neural audio codec, low frame rate, speech tokenization, residual vector quantization, intelligibility degradation

## 核心痛点
低帧率（≤6.25 Hz）神经音频编解码器在自回归语音合成中可显著降低推理计算成本，但其质量退化机制尚未被充分理解。已有工作将6.25 Hz处的性能悬崖归因于音素碰撞（一个帧内包含多个音素），但缺乏深入验证。

## 方法创新
本文通过控制变量消融实验，系统研究低帧率退化的真正原因：
- 固定训练策略：对比固定裁剪时长（0.38秒）与固定token序列长度两种训练配置。
- 假设检验：量化评估音素碰撞和码本饱和两种假说。
- 框架：基于DAC（16 kHz），保持架构和码本大小（12级RVQ，码本1024）不变，仅改变帧率（1.6~100 Hz）。

## 实验结果
- 固定时长训练下，6.25 Hz处出现WER从10.62%飙升到107.4%的“悬崖”，证实已有观察。
- 固定token序列长度后，此悬崖消失，WER随帧率降低平滑上升，至1.6 Hz仍可理解。
- 音素碰撞和码本饱和假说均未表现出根本性瓶颈：码本利用率并未骤降，且固定序列长度后WER与每帧音素数线性相关。
- 参考编解码器对比（DAC、Mimi、BigCodec等）显示：低帧率专用设计（如Mimi的Transformer bottleneck）可缓解退化，但非必要。

## 一句话评价
本文揭示了低帧率编解码器退化的真正原因在于训练时token数量不足，而非帧率本身的固有限制，为极低帧率（≤3.125 Hz）的实用化铺平了道路。

---

## 22. Joycent: Diffusion-based Accent TTS without Accented Phone Prediction

**作者**: Xintong Wang, Ye Wang
**链接**: [2606.16417](https://arxiv.org/abs/2606.16417)
**分类**: Text-to-Speech | **关键词**: Accent TTS, Diffusion, Disentanglement, Whisper, Conditional Layer Normalization, Gradient Reversal Layer

# Joycent: Diffusion-based Accent TTS without Accented Phone Prediction

## 核心痛点
- 现有口音TTS系统（如两阶段流水线）依赖将标准音素序列转换为口音音素序列，导致错误累积，且需要大量配对的标注数据，难以获取。
- 文本级口音表示无法捕捉声学口音特征（如韵律、节奏），生成语音自然度受限。

## 方法创新
- 提出**Joycent**，基于扩散模型的口音TTS，直接由标准音素序列和语音参考（口音参考+说话人参考）合成口音语音，无需显式的口音音素预测。
- 引入**WhisAID**（基于Whisper的口音识别模型），通过梯度反转层（GRL）解耦口音与说话人信息，提取纯净的口音嵌入。
- 利用**FACodec**提取说话人嵌入，实现零样本说话人适应。
- 在文本编码器的Conformer块中使用**条件层归一化（CLN）**，将口音和说话人信息与语言表示融合。

## 实验结果
- 在口音度（accentedness）指标上优于基线系统（如MacST、AccentBox），同时在seen-speaker和unseen-speaker设置下均能较好保持说话人身份。
- 消融实验验证了GRL和CLN对解耦和口音渲染的有效性。

## 一句话评价
Joycent通过扩散模型和解耦表示，实现了无需口音音素预测的高质量口音TTS，兼具口音自然度与说话人保真度。

---

## 23. An Asymmetric Formula for Interval Consonance and its Relation to Harmonic Coincidence

**作者**: David De Roure
**链接**: [2606.16412](https://arxiv.org/abs/2606.16412)
**分类**: Music Information Retrieval / Computational Musicology | **关键词**: consonance, Euler's Gradus Suavitatis, harmonic coincidence, asymmetric formula, interval dissonance

## 核心痛点
Euler的Gradus Suavitatis对称处理分子和分母，但人类对音程的感知是非对称的（低音与高音角色不同），且该公式在13个标准音程数据上出现三重并列，无法区分某些重要音程（如小三度、小六度、大二度）。

## 方法创新
提出非对称公式 f(p/q) = p + Ω*(q)，其中p为分子（高音），q为分母（低音），Ω*(n) = Σ e_i(p_i - 1) 为加权素因子指数和。该公式将高音视为谐波序列中的位置，低音视为素复杂度，并引入两阶段感知解释。此外，证明Euler公式可解释为加权谐波重合计数，权重为 Ω*(n)。

## 实验结果
在13个标准音程的人类协和度排名上（Krumhansl数据），f公式的Spearman ρ=0.989，优于Euler公式的0.979，与max(p,q)相同，但f解决了Euler的三重并列，仅留下一个两重并列（小六度与大二度）。对三全音（45/32）的区分更为显著（f=50 vs Euler的14）。

## 一句话评价
该工作通过非对称算术公式更好地拟合了人类音程协和度感知，并揭示了与谐波重合模型的深层联系，具有理论简洁性和实证优势。

---

## 24. ArtBoost: Synthetic Articulatory Data Augmentation for Acoustic-to-Articulatory Inversion

**作者**: Hyung Kyu Kim, Byungchan Hwang, Hak Gu Kim
**链接**: [2606.16327](https://arxiv.org/abs/2606.16327)
**分类**: Acoustic-to-Articulatory Inversion | **关键词**: acoustic-to-articulatory inversion, data augmentation, speech–mesh, Electromagnetic Articulography, 3D facial animation

## 核心痛点
传统声学-发音反演（AAI）模型依赖电磁发音描记术（EMA）数据，采集成本高、规模有限，导致模型泛化能力不足。

## 方法创新
提出ArtBoost，利用大规模语音-3D面部网格数据集（如TFHP）生成伪发音轨迹。流程包括：
1. ASR引导的语句分割，将长视频切分为与EMA数据集兼容的语句级片段。
2. 从面部网格中追踪可见发音器官（上唇、下唇、下切牙）的运动轨迹，转换为12通道伪标注。
3. 预训练AAI模型（仅监督可见通道），然后在真实EMA数据上微调（全通道监督）。

## 实验结果
- HPRC数据集：PCC提升+2%（0.678→0.698），RMSE降低。
- USC-TIMIT数据集：PCC提升+25%（0.351→0.510），RMSE显著下降。
- 在不同AAI架构上均表现稳定收益。

## 一句话评价
ArtBoost通过大规模合成数据缓解了AAI数据稀缺问题，方法简洁有效，具有较好的可扩展性。

---

## 25. NVMOS: Non-Verbal Vocalization Quality Assessment in Speech

**作者**: Jialong Mai, Jinxin Ji, Xiaofen Xing, Wencui Liu, Xiangmin Xu
**链接**: [2606.15888](https://arxiv.org/abs/2606.15888)
**分类**: Speech Quality Assessment | **关键词**: non-verbal vocalization, speech quality assessment, MOS prediction, speech representation, multimodal large language models

## 核心痛点
现有语音质量评估方法通常关注整体自然度，而非语言发声（Non-verbal vocalizations, NVs）的评估主要检查类型和位置正确性，忽略了NV事件自身的感知质量。通用多模态大语言模型（如Gemini）在NV质量评估中与专家评分不一致，无法可靠替代人工判断。

## 方法创新
- 构建NV-MOS数据集：包含7,784个样本（约9.51小时），涵盖16种NV类别，包括合成NV-TTS输出和自然NV样本，由三位声学专家按0-5分制评分。
- 提出NVMOS模型：首个专门预测语音中NV事件感知质量的模型。采用文本查询局部聚焦模块，以标记文本（如[ahem]）为查询，通过跨注意力机制聚焦于帧级语音表示中的相关局部区域，从而预测NV质量分数。

## 实验结果
- 在NV-MOS测试集上，NVMOS（使用WavLM Large特征）的Pearson相关系数达0.697，Spearman为0.657，Kendall为0.518，MAE为0.837，达到或超过专家间一致性水平（专家间Pearson为0.589-0.699）。
- 与LLM judges对比，最佳LLM（Gemini 3 Flash）的Pearson仅0.468，远低于NVMOS。

## 一句话评价
NVMOS是首个能够可靠预测语音中非语言发声感知质量的专用模型，通过局部事件聚焦设计实现了与专家评分高度一致的性能。

---

## 26. Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models

**作者**: Hyebin Cho, Jaehyuk Jang, Changick Kim, Joon Son Chung
**链接**: [2606.15751](https://arxiv.org/abs/2606.15751)
**分类**: Audio Classification / Audio Language Model | **关键词**: Acoustic Prompting, Few-Shot Learning, Audio Language Model, Prompt Learning, Stage-wise Modulation, CLAP

## 核心痛点
现有音频语言模型（ALM）的提示学习主要集中在文本编码器上，忽略了音频编码器侧的可学习提示潜力，导致跨模态对齐受限，难以适应少样本音频分类任务。

## 方法创新
提出音频侧提示学习（ASPL）框架，在音频编码器的三个关键阶段注入可学习的连续提示向量（仿射变换），实现阶段式调制：
1. **频谱调制**：在log-mel频谱图上进行频率维度的缩放（类似可学习均衡器）。
2. **令牌级提示**：在Patch Embedding后的令牌特征上进行通道维度的重校准。
3. **结构提示**：在首个Swin Transformer块的输出上进行早期层条件化。
该模块可与现有文本侧提示方法（如CoOp、CoCoOp、PALM）即插即用，参数高效（共享类间参数）。

## 实验结果
在11个数据集上的16-shot设置下，ASPL*（完整三阶段）平均提升约1.1%的Top-1准确率，且参数开销极小。与PALM结合时，平均准确率从77.86%提升至79.26%。

## 一句话评价
通过对称地在音频编码器侧引入轻量级阶段性调制，有效弥补了文本中心提示方法的不足，为少样本音频分类提供了一种高效互补方案。

---

## 27. AP-GRPO: Anchor-Gated Phonetic Alignment with Policy Optimization for Pathological Speech Reconstruction

**作者**: Pengfei Zhang, Hoang H Nguyen, Yutong Song, Wenjun Huang, Tahmid Imtiaz Imu, Henry Peng Zou, Jiang Wu, Honghui Xu, Amir M. Rahmani
**链接**: [2606.15540](https://arxiv.org/abs/2606.15540)
**分类**: Pathological Speech Reconstruction | **关键词**: 病理语音重建, GRPO, 锚点门控, 音素对齐, 软动态时间规整, 语音语言模型

## 核心痛点
病理语音（如帕金森病、ALS等）常存在不均匀退化：部分词语清晰（锚点），其余区域严重失真。现有方法（SFT、句子级GRPO）无法区分忠实重建与流畅改写，且依赖大量配对数据。

## 方法创新
提出AP-GRPO框架，包含：
- **锚点门控奖励**：保留可靠的可听锚点；
- **帧间音素对齐奖励**：通过病理风格文本到音素路径（TTDS）与原始语音的音素后验图（PPG）进行软动态时间规整（Soft-DTW）匹配，衡量重建内容的音素支持度。
该框架无需参考文本，直接利用患者自身语音信号作为对齐目标。

## 实验结果
在ALS、脑瘫、痴呆、帕金森四种疾病上，AP-GRPO显著提升重建忠实度：最严重条件下词错误率（WER）从0.75降至0.29。同时有效抑制幻觉插入，适应不同疾病严重性而不需手动调参。

## 一句话评价
首个将组相对策略优化（GRPO）与音素对齐结合用于病理语音重建的方法，利用锚点结构实现自适应且可解释的语音恢复。

---

## 28. Beyond Classification: A Cough Regression Benchmark for Respiratory Acoustic Foundation Models

**作者**: Mayur Sanap, Prasanna Desikan, Edgar Lobaton
**链接**: [2606.15436](https://arxiv.org/abs/2606.15436)
**分类**: Respiratory Acoustic Foundation Models | **关键词**: Cough Regression, Foundation Models, Respiratory Acoustics, Transfer Learning, Regression Heads

## 核心痛点
现有呼吸声学基础模型（FM）在咳嗽分类任务上表现优异，但对其从咳嗽音频中预测连续健康指标（如年龄、BMI、疾病概率）的能力几乎没有探索。先前研究仅评估单一模型、线性探测，缺乏多模型比较、非线性头评估和跨数据集泛化。

## 方法创新
本文提出了一个多模型、多目标的咳嗽回归基准，评估五种冻结的FM（OPERA-CT, OPERA-CE, OPERA-GT, HEAR, M2D+RESP）在三个数据集（CIDRZ、Coswara、CoughVID）上的六个回归目标（年龄、BMI、X光异常概率、结核概率）。比较了三种回归头：线性、MLP-small（256单元瓶颈+dropout）和全MLP。采用受试者分离协议，报告MAE并与均值预测基线（MAD）对比。

## 实验结果
- 在所有任务中，模型均超越了均值基线，但CIDRZ上的信号微弱（最佳MAE/MAD≥0.92）。
- MLP-small在30个模型×任务组合中的23个上优于线性探测，全MLP在小数据集CIDRZ上过拟合（M2D+RESP MAE增加0.53年），但在大数据集CoughVID上恢复。
- 生成式预训练（OPERA-GT）在年龄回归上整体优于对比式（OPERA-CT），在Coswara和CoughVID上差异显著。
- 跨数据集迁移存在强不对称性：大而多样的数据集（CoughVID）泛化到小临床数据集（CIDRZ）良好（-0.17年），但反向失败（CIDRZ→Coswara +2.43年）。
- 低数据区间分析：HEAR和M2D+RESP在N=50时达到近全性能，而OPERA模型需要N=400。

## 一句话评价
本文系统评估了呼吸声学基础模型在咳嗽连续量回归上的能力，揭示了模型、头容量与数据集大小之间的权衡，为低资源临床部署提供了指导。

---

## 29. FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing

**作者**: Yuxuan Jiang, Mingyang Han, Yusheng Dai, Andong Wang, Tianhong Zhou, Jiaxin Ye, Dongxiao Wang, Haoxiang Shi, Boyu Li, Jun Song, Cheng Yu, Bo Zheng, Weibei Dou, Zehua Chen, Jun Zhu
**链接**: [2606.15186](https://arxiv.org/abs/2606.15186)
**分类**: Audio Editing | **关键词**: audio editing, training-free, rectified flow, attention decoupling, temporal consistency, background preservation

# FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing

## 核心痛点
现有文本到音频（TTA）生成虽进步显著，但音频编辑面临两大挑战：时间一致性（仅修改目标区域）和背景保持（非编辑背景音不变）。由于音频的叠加特性，现有方法难以解耦重叠声音，导致修改特定部分时引起整个音频的意外变化。基于训练的方法需构建复杂三元组数据集或依赖专用架构，计算开销大且灵活度低。

## 方法创新
1. **优化反转-逆过程**：利用Rectified Flow（RF）的直线概率流，减少反转误差，提升音频重构质量，为编辑提供高保真基础。
2. **文本-音频注意力图时序提取**：利用MM-DiT双块中的文本-音频注意力图，在前5个反转步骤中聚合交互分数，生成二进制时间掩码M，精确定位编辑区域。
3. **调度注意力解耦**：在MM-DiT单块中实施三阶段调度策略：
   - **阶段1（特征混合）**：早期通过动态系数δ（0.85→1.0）插值源和目标KV特征，并利用掩码M对非编辑区域完全注入源特征。
   - **阶段2（时序控制）**：中期δ=1，仅由目标提示引导语义生成，严格掩码限制编辑区域。
   - **阶段3（全局协调）**：后期恢复标准自注意力，实现编辑与未编辑部分的和谐过渡。
4. **任务导向噪声注入**：在目标区域潜在分布中注入随机噪声，减少原始声学特征残留，增强对音频移除和非刚性替换等任务的处理能力。

## 实验结果
通过定量和主观实验，FreeSonic在多种音频编辑任务中实现了高保真度和一致性。消融研究证实了各组件的贡献，效率分析显示推理速度优于现有模型。

## 一句话评价
首次将RF反转引入免训练音频编辑框架，通过时序感知解耦注意力实现了精准、一致的音频编辑，兼顾时间一致性与背景保持。

---

## 30. AUDEDIT: Inversion-Free Text-Guided Editing with Pretrained Audio Flow Models

**作者**: Zhongyuan Fu
**链接**: [2606.15149](https://arxiv.org/abs/2606.15149)
**分类**: 文本引导音频编辑 | **关键词**: 文本引导音频编辑, 无反转编辑, 整流流, Stable Audio 3, 音频生成, 速度场差异

# AudEdit: 无反转文本引导音频编辑

## 核心痛点
现有基于反演的音频编辑方法（如SDEdit、ODE反演）需要在噪声状态下折中：浅噪声保留源细节但编辑不足，深噪声增强语义但破坏瞬态、节奏、音色等感知细节。缺乏直接保留源结构的同时实现语义变化的方法。

## 方法创新
提出AudEdit，一种无需训练、无需反转的文本引导音频编辑框架，基于预训练的整流流音频生成器（Stable Audio 3）。核心思路：直接构造源到目标的ODE路径，在每个流步骤中，比较目标条件和源条件的速度场（在共享随机源边际下），并利用它们的差异更新编辑潜变量。不经过噪声状态，无需优化或注意力图访问。

## 实验结果
在FSD50K音效集和Song Describer Dataset音乐集上，AudEdit相比SDEdit、ODE反演和FireFlow三个强基线，在CLAP文本对齐和音频保留方面均取得一致提升。例如，音效集上目标文本CLAP相似度从0.42提升至0.52，FAD从65.70降至50.37。

## 一句话评价
AudEdit通过无反转的源到目标速度差分流编辑，在保留音频细节的同时显著提升编辑语义对齐，为文本引导音频编辑提供了高效、无需训练的解决方案。

---

## 31. When the Same Musical Knowledge Forgets Differently: A Clean Probe of Pathway-Dependent Forgetting

**作者**: Yu Liu, Zhiwei Yang, Wenxiao Zhang, Cong Cao, Fangfang Yuan, Kun Peng, Haimei Qin, Lei Jiang, Jin B. Hong, Hao Peng, Yanbing Liu
**链接**: [2606.15088](https://arxiv.org/abs/2606.15088)
**分类**: Error | **关键词**: 

总结生成失败: 'utf-8' codec can't encode character '\ud835' in position 11587: surrogates not allowed

---

## 32. Interpretable and Frugal Learning Systems Employing Multiresolution Pyramids and Volterra Kernels

**作者**: Kishore Kumar Tarafdar
**链接**: [2606.15011](https://arxiv.org/abs/2606.15011)
**分类**: 可解释深度学习与信号处理 | **关键词**: 多分辨率金字塔, Volterra核, 可解释性, 节俭学习, 小波变换, 剪切波变换, 微波辐射计反演, 图像分割, 脑MRI分割

## 核心痛点
深度学习模型处理多维信号时，学习到的表示缺乏显式信号结构且难以检查，导致可解释性差。

## 方法创新
1. 提出基于信号理论的节俭学习系统，结合多分辨率分析、小波滤波器组、Volterra核和非线性计算图。
2. 将尺度、方向几何、记忆和非线性交互表示为可微算子模块，通过反向传播训练。
3. 实现GPU兼容的L维卷积层、多速率采样层、高阶Volterra核层（在自然域和双正交小波系数域）以及有理多项式线性-非线性级联头。
4. 开发稳定性约束的多维IIR滤波器、完美重构快速离散小波变换（FDWT）和快速数字剪切波变换（FDST）滤波器组层。
5. 提出多分辨率子带视觉变换器WaveletViT和ShearViT，用于分割任务。

## 实验结果
- 微波辐射计反演：InVeRt 3/3模型在28,052个测试样本上，水汽密度RMSE 0.61 g/m³，温度RMSE 1.15 K。
- 分类：谱图滤波器组编码器将ESC-20音频基线从22%提升至82%平均准确率；Volterra头用更少参数达到可比性能。
- MRI分割：ShearNETR 3D在颅骨剥离、灰质、白质、脑脊液和病变分割的IoU分别为0.98、0.86、0.90、0.71和0.60，参数量4.52M。

## 一句话评价
该论文通过多分辨率滤波器组和Volterra核构建可解释、节俭的深度学习系统，在多个应用领域实现了高性能与紧凑表示。

---

## 33. An Empirical Study on Learning Latent Representations for Emotional Speech Synthesis

**作者**: Vinh Dang Quang, Huy Ngo Quang
**链接**: [2606.14922](https://arxiv.org/abs/2606.14922)
**分类**: Text-to-Speech | **关键词**: 情感语音合成, FastSpeech 2, 说话人适应, 韵律瓶颈, 潜表示学习

## 核心痛点
生成具有情感表达的自然语音，特别是在单一说话人情感合成和跨说话人风格迁移（目标说话人仅有中性数据）任务中，控制语音的表现力和自然度是主要挑战。

## 方法创新
- **基础模型**：基于 FastSpeech 2 进行修改，引入情感嵌入（子任务1）或情感嵌入+说话人嵌入+韵律瓶颈（子任务2）。
- **子任务1**：使用情感 ID 查找表生成固定长度向量，与编码器输出相加。
- **子任务2**：说话人嵌入与编码器输出拼接后投影，情感嵌入经线性层+tanh后相加，再通过韵律瓶颈（带残差连接）。
- **数据预处理**：使用 Facebook Denoiser 去噪，ASR 校对文本，替换英文单词为越南语读音。

## 实验结果
- **子任务1**：自然度 MOS 2.719/5，音节错误率 72.40%。
- **子任务2**：自然度 MOS 1.622/5，音节错误率 64.80%，说话人相似度 1.543/4。

## 一句话评价
通过潜表示学习，该方法在 VLSP 2022 情感语音合成任务中展现出潜力，但自然度仍有提升空间。

---

## 34. Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models

**作者**: Yuxuan Chen, Haoyuan Yu, Peize He
**链接**: [2606.14820](https://arxiv.org/abs/2606.14820)
**分类**: Spatial Audio / Self-Supervised Learning / Computational Psychoacoustics | **关键词**: binaural masking level difference, spatial audio, self-supervised learning, representation learning, computational psychoacoustics

### 核心痛点
现有空间自监督音频模型在宏观声源定位任务上表现优异，但未能验证它们是否真正编码了微观的耳间相位精细结构（微秒级），而非依赖简单的启发式策略（如频谱时间干扰纹理）。

### 方法创新
1. **心理声学基准**：基于双耳掩蔽级差（BMLD）设计评估协议，直接探测冻结模型内部表示对交变相位（SπN0）与同相（S0N0）信号的区分能力。
2. **控制实验**：采用比特精确噪声共享协议确保掩模波形完全一致；设置单耳SSL负控制（HuBERT-L、WavLM-L、Wav2Vec2-L、DAC）证明BMLD效应需双耳输入。
3. **物理消融**：高通滤波、梅尔能量均衡、50 Hz包络声码器逐步剥离检测机制，区分真实相位编码与包络纹理依赖。

### 实验结果
- 单耳控制模型在所有条件下BMLD=0 dB，确认双耳特异性。
- 通用双耳SSL模型（WavJEPA、GRAM-T）在500 Hz、SNR=-14 dB时BMLD仅+0.5 dB和+2.1 dB，远低于EC基准+15.7 dB，表现出极弱相位敏感性。
- 专用空间双耳SSL模型（Spatial-AST、DSpAST）达到+6.8~+7.0 dB，但仍低于EC基准。
- 消融实验表明：GRAM-T在2 kHz以上高通滤波后检测率仍100%，梅尔能量均衡后100%，但声码器处理后降至75%，表明其依赖快速包络纹理而非相位精细结构。
- 生态效度实验（基于真实BRIR）显示，语音刺激下所有双耳模型检测率显著高于纯音，反映对宽带包络的混淆依赖。

### 一句话评价
该工作通过严格的BMLD基准暴露了当前空间音频基础模型在真实相位编码上的根本缺陷，揭示了模型依赖频谱时间干扰纹理而非跨通道相位计算的机制，为未来研究指明了方向。

---

## 35. Unifying Acoustic Features and Text with Multimodal LLMs for Neurodegenerative Screening

**作者**: Qingfeng Zhang, Yuanxiong Guo, Yanmin Gong
**链接**: [2606.14788](https://arxiv.org/abs/2606.14788)
**分类**: Speech-based Disease Screening | **关键词**: Neurodegenerative diseases, Large language models, Multimodal learning, Voice biomarkers, Alzheimer's disease, Parkinson's disease

## 论文总结

### 核心痛点
- 现有基于语音的神经退行性疾病筛查方法大多仅依赖转录文本，未能有效整合声学特征（如语谱图、MFCC）与语言、人口统计信息。
- 许多LLM系统使用分类头将池化表示映射到固定标签空间，导致决策层僵化，难以跨任务泛化。

### 方法创新
- 提出**NeurMLLM**框架，采用多模态架构：使用视觉Transformer（ViT）编码语谱图和MFCC，通过投影层对齐到LLM嵌入空间，与转录文本和人口统计指令拼接为统一序列。
- 利用**LoRA**高效微调LLM，将分期任务转化为**约束标签token生成**（生成式分类），避免传统分类头。
- 在Bridge2AI-Voice数据集上对阿尔茨海默病（AD）和帕金森病（PD）进行细粒度分期（AD: CN/MCI/AD；PD: 健康/早期/晚期）。

### 实验结果
- NeurMLLM在AD和PD分期任务上均**一致优于**传统机器学习和现有基于LLM的方法（包括使用分类头的方法）。
- 有效融合声学、语言和人口统计信息，提升分期准确性。

### 一句话评价
提出了一种高效的多模态LLM框架，通过生成式分类统一声学与文本特征，实现了对神经退行性疾病的高精度分期。

---

## 36. LLM-Based Synthetic Ground Truth Generation for Audio-Based Emotion Classification via In-Context Learning

**作者**: Qing Huang, Pooja Pol, Jianing Zhang
**链接**: [2606.14784](https://arxiv.org/abs/2606.14784)
**分类**: Speech Emotion Recognition / Audio Emotion Classification | **关键词**: Large Language Models, In-Context Learning, Synthetic Ground Truth, Affective Computing, Virtual Reality, Speech Emotion Recognition

# 论文总结

## 核心痛点
- VR协作环境中，语音情感标注困难：传统自我报告主观且延迟，人工标注成本高，传感器数据噪声大。
- 缺乏跨会话一致的自动标注方法。

## 方法创新
- 提出基于大语言模型（LLM）的合成情感标注框架，利用上下文学习（ICL）无需微调。
- 采用**声学相似性检索**指导ICL示例选择：使用韵律描述符（音高、响度、强度、语速）进行检索，而非随机采样。
- 多模态融合：声学特征用于检索，文本转录由LLM语义推理，实现跨会话情感对齐。
- 使用Voxtral语音LLM，模块化设计可替换其他语音LLM。

## 实验结果
- 在多人VR录音数据集上评估，展示了可扩展、数据高效的潜力。
- 与基于词典的NRC-VAD方法对比，检索引导ICL提高了标注一致性。

## 一句话评价
该工作通过声学相似性引导的上下文学习，实现了无需微调的跨会话语音情感合成标注，为VR协作场景提供了高效的数据驱动决策支持。

---

