# Arxiv Daily Deep Report - 2026-06-30

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 14
---

## 1. MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling

**作者**: Yoonjeong Park, Jaekwon Im, Juhan Nam
**链接**: [2606.30580](https://arxiv.org/abs/2606.30580)
**分类**: Singing Voice Editing | **关键词**: Singing voice editing, Duration modeling, Audio infilling, Flow-matching, Melody-aware

# 论文总结：MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling

## 核心痛点
- 文本驱动的歌声编辑（SVE）需在修改歌词的同时严格保持原始旋律、总时长和非编辑区域，但现有方法（如隐式建模无法硬约束时长，显式建模EditSinger缺乏旋律感知）常导致时长偏移、旋律不一致或编辑边界不自然。

## 方法创新
- 提出**MeloDISinger**，基于flow-matching的SVE模型，实现旋律感知和时长保持的编辑。
- **核心模块MeloDRP**：预测固定预算的时长比例而非绝对时长，通过跨注意力融合音素信息与伪MIDI旋律上下文，并引入时序重叠监督实现软性音素-音符对应，确保编辑跨度总时长严格不变。
- **Flow-matching mel解码器**：以音频填充方式合成编辑区域，保留非编辑区域并实现无缝边界过渡。
- **自动评价集生成管道**：利用WhisperX和LLM生成满足音节容量的编辑歌词，避免不可行编辑。

## 实验结果
- 在GTSinger-En数据集上，与EditSinger和Veo2对比，在替换、插入、删除和混合场景下，MeloDISinger在**词错误率（WER）**、**时长偏差（DDUR）**和**F0一致性（FPC）**上均达SOTA，特别是时长偏差严格为0，EditSinger和Veo2均存在偏差。
- 主观评估也显示更优的自然度和旋律保持。

## 一句话评价
MeloDISinger通过旋律感知的时长比例预测和flow-matching音频填充，首次在歌声编辑中实现了严格时长保持与高质量编辑，显著优于现有方法。

---

## 2. Evaluation of Head-Related Transfer Functions Across Five Levels of Individualisation in Virtual Reality

**作者**: Ludovic Pirard, Katarina C. Poole
**链接**: [2606.30114](https://arxiv.org/abs/2606.30114)
**分类**: Spatial Audio / HRTF Individualization | **关键词**: HRTF, sound localisation, virtual reality, individualisation, synthetic HRTF, photogrammetry, KEMAR

# 论文总结

**核心痛点**：个体 HRTF 获取困难，通用 HRTF 和合成 HRTF 的性能缺乏在同一实验框架下的系统比较。

**方法创新**：通过两个 VR 定位实验，在 19 名受试者中比较了五种 HRTF 条件（个体测量、KEMAR、随机非个体、高分辨率扫描合成、摄影测量合成），并验证了重测信度。

**实验结果**：侧向定位指标对 HRTF 类型不敏感，而极坐标指标和混淆率表现出强依赖性；随机 HRTF 优于 KEMAR；高分辨率合成 HRTF 的性能与个体测量相当；摄影测量合成 HRTF 和 KEMAR 的性能最差。

**一句话评价**：首次在同一 VR 定位协议中全面比较五种个性化水平的 HRTF，为非个体基线选择提供了实用指导，并强调了网格分辨率对仰角定位的重要性。

---

## 3. Semi-Supervised Sound Event Detection with Conditional Mixup and Embedding-Level Contrastive Loss

**作者**: Nian Shao, Xian Li, Xiaofei Li
**链接**: [2606.29901](https://arxiv.org/abs/2606.29901)
**分类**: Sound Event Detection | **关键词**: sound event detection, semi-supervised learning, contrastive learning, mixup, ATST

## 核心痛点
声音事件检测（SED）受限于标注数据稀缺，现有半监督方法依赖一致性正则化，但对基于大规模预训练自监督编码器的系统效果不佳。

## 方法创新
1. **条件混合（Conditional Mixup）**：统一组合混合（composition mixup，λ∈[0.5,τ]）和扰动混合（perturbation mixup，λ∈(τ,1]），分别用于伪标签学习和对比学习，解决两种目标对混合的不同需求。
2. **嵌入级对比损失**：借鉴ATST-Frame的帧级自监督对比目标，在半监督微调中引入嵌入级对比损失（包括组合和扰动两种情况），充分利用无标签数据。
3. **两阶段微调**：第一阶段冻结ATST-Frame，优化CRNN和分类器；第二阶段使用条件混合及相应伪标签损失和对比损失联合微调所有参数。

## 实验结果
在DESED验证集上，ATST-SEDv2达到0.645 PSDS1和0.822 PSDS2（cSEBB后处理），建立新SOTA。

## 一句话评价
本文通过条件混合统一了混合策略，并引入嵌入级对比损失，显著提升了半监督SED的性能。

---

## 4. VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition

**作者**: Piyush Arora, Navlika Singh, Umberto Cappellazzo, Stavros Petridis, Maja Pantic
**链接**: [2606.29632](https://arxiv.org/abs/2606.29632)
**分类**: Audio-Visual Speech Recognition | **关键词**: Audio-Visual Speech Recognition, LLMs, Variational Information Bottleneck, Noise Robustness

## 核心痛点
现有基于LLM的音视频语音识别（AVSR）模型在干净条件下表现优异，但面对噪声环境时性能显著下降。原因在于LLM骨干网络预训练于纯文本数据，微调时仅更新少量参数（LoRA），缺乏对噪声鲁棒性的显式建模，导致音频编码器输入的噪声会直接污染LLM的内部表示。

## 方法创新
本文提出**VIB-AVSR**，通过将变分信息瓶颈（VIB）层插入LLM的指定层（实验表明第4层和第8层最优），对音频隐藏状态进行压缩。VIB层由两层MLP实现，输出高斯分布的均值和方差，并通过重参数化采样得到瓶颈表示，再与原始表示插值（α=0.5）后传入后续层。训练时优化VIB目标：最大化转录似然的同时，最小化KL散度以压缩与任务无关的噪声信息。无需修改架构或额外数据，仅增加少量计算。

## 实验结果
在LRS2数据集上，与基线Llama-AVSR相比：
- **有噪声训练**：在多噪声类型（babble、speech）和SNR（-10到5dB）下，WER平均降低1-2个百分点（如babble噪声下平均WER从18.85%降至17.39%）。
- **干净训练**：同样有提升，且在极端噪声（-10dB）下增益更明显（如speech噪声下WER从42.13%降至37.44%）。
- 在无噪声条件下性能几乎不变（WER≈2.4%）。

## 一句话评价
一种轻量级、即插即用的方法，通过变分信息瓶颈机制显著提升LLM-based AVSR模型对噪声的鲁棒性，且不牺牲干净语音性能。

---

## 5. DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection

**作者**: Hoyeol Sohn, Juhan Nam
**链接**: [2606.29480](https://arxiv.org/abs/2606.29480)
**分类**: Neural Speech Codec / Audio Compression | **关键词**: speech codec, variable frame rate, token masking, low bitrate, speech tokenization, path length equalization

## 核心痛点
现有神经语音编解码器通常采用固定帧率（FFR），在静音或平稳段浪费比特，在语音快速变化段分辨率不足。可变帧率（VFR）编码通过自适应分配帧率来改善效率，但需要传输位置/时长的边信息，导致总比特率公平比较下VFR增益不明显。此外，现有VFR方法在边界选择、边信息设计和可控实验上存在不足。

## 方法创新
1. **动态令牌掩码（DTM）**：在编码器两阶段之间，保留选中的令牌（通过边界选择器），并用可学习的<MASK>填充被掩码位置。传输1比特/帧的二值掩码作为位置边信息，实现位置感知解码。相比合并/池化操作，该方法在相同比特率下取得最优重建。
2. **路径长度均衡（PLE）**：一种线性时间O(N)的边界选择器，将编码器特征沿时间轴的累积变化量等分，产生分布均匀的自适应片段。相比VARSTok、FlexiCodec、CodecSlime中的启发式/优化方法，PLE在质量和效率之间取得更优权衡。
3. **严格匹配总比特率的实验**：在统一训练和评估协议下，将内容比特和边信息比特都计入总比特率，在低到高频点进行VFR与FFR的公平对比，证明VFR在低/中比特率下具有广泛优势。

## 实验结果（根据摘要推断）
DTM-Codec（127M参数，LibriSpeech-960训练）在匹配总比特率下，重建质量和可懂度全面优于FFR基线。尽管模型规模和训练数据小于BigCodec、X-Codec 2.0等，但在多个指标上达到或超越它们。代码开源。

## 一句话评价
DTM-Codec通过动态令牌掩码和高效边界选择，在严格匹配总比特率下首次展示了VFR对FFR的可靠且广泛的重建增益。

---

## 6. VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion

**作者**: Sujin Koo, Sangyoon Kim, Ji Sub Um, Hoirin Kim
**链接**: [2606.29450](https://arxiv.org/abs/2606.29450)
**分类**: Audio Enhancement | **关键词**: noise-robust bandwidth expansion, flow matching, velocity contrastive regularization, representation alignment, self-supervised learning

## 核心痛点
噪声鲁棒带宽扩展（NR-BWE）旨在从带噪低分辨率输入重建高质量宽带语音，但现有方法难以兼顾高频重建和噪声抑制。标准流匹配目标仅提供单向监督，噪声下速度估计模糊，导致生成轨迹偏离干净语音流形。

## 方法创新
提出 VeRe-Flow，一种基于流匹配的清洁引导框架，引入多级清洁监督：
1. **速度对比正则化（VeCoR）**：双向监督，吸引预测速度朝向干净轨迹，排斥远离噪声轨迹。
2. **表示对齐（REPA）**：将中间特征与干净自监督学习（SSL）表示对齐，促进噪声不变语义特征。
3. **架构改进**：集成卷积残差模块和噪声鲁棒SSL条件（XEUS）作为额外语义引导。

## 实验结果
在Valentini-Botinhao数据集上，VeRe-Flow在LSD、DNSMOS OVRL和MOS上均超越所有基线（包括生成式和非生成式）。具体：LSD最低（1.10），DNSMOS OVRL最高（3.12），MOS最高（4.14）。

## 一句话评价
VeRe-Flow通过速度对比和表示对齐有效引导流匹配生成干净语音，在NR-BWE任务上达到SOTA。

---

## 7. GigaSpeechBench: A Real-World Multilingual Speech-to-Text Benchmark

**作者**: Yujie Tu, Yifan Yang, Tianrui Wang, Yanqiao Zhu, Guodong Lin, Mingchen Shao, Haoran Wang, Junzhe Liu, Yuxiang Fu, Yizhou Peng, Changsong Liu, Peng Wang, Zhikang Niu, Yunchong Xiao, Haolong Zheng, Xiuwen Zheng, Xulin Fan, Wei-Qiang Zhang, Lei Xie, Longbiao Wang, Eng-Siong Chng, Jiajun Zhang, Kele Xu, Jianwei Yu, Binbin Zhang, Jiayu Du, Wupeng Wang, Zhigao Chen, Yunlong Wu, Guoguo Chen, Xipeng Qiu, Mark Hasegawa-Johnson, Kai Yu, Zhifu Gao, Xiangang Li, Xie Chen
**链接**: [2606.28884](https://arxiv.org/abs/2606.28884)
**分类**: Speech Recognition | **关键词**: 多语言ASR, 低资源语言, 方言, 口音, 术语密集, 年龄变化, 基准, 真实世界, 中东语言, 东南亚语言

## 核心痛点
- 现有ASR基准在高资源语言上表现良好，但在真实场景中鲁棒性不足，缺乏对低资源语言（尤其中东和东南亚，覆盖超过10亿人口）、方言、口音、术语密集语音以及年龄变化（老年人和儿童）的全面评估。
- 现有基准多使用干净条件下的朗读语音，缺少自发会话、重叠语音、背景噪声、远场录音等声学多样性。
- 评估资源分布不均，中东和东南亚语言被严重忽视；术语密集专业领域（如医学、法律、金融）以及老年和儿童语音的评估几乎缺失。

## 方法创新
- 构建了**GigaSpeechBench**，一个680小时人工标注的多语言、多维度野外ASR & AST基准，涵盖五个模块：
  1. 14种语言/区域：7个阿拉伯语方言区、5个东南亚语言、2个东亚语言（日语和韩语），每种20小时；其中11种语言提供中文和英文翻译参考。
  2. 6种汉语方言：湘、晋、赣、闽、粤、吴，每种10小时。
  3. 6种英语口音：中文、印度、日本、菲律宾、苏格兰、新加坡英语，每种10小时。
  4. 12个术语密集领域：农业、AI、艺术、生物技术、电商、工程、娱乐、金融、人文、法律、医学、军事，每个领域中文和英文各10小时，并配有热词列表。
  5. 2个年龄组：老年人和儿童语音，中文和英文各10小时。
- 所有语音来自真实野外条件下的自发语音，而非朗读或合成语音。
- 提供统一的评估协议，便于直接比较不同模型的性能。

## 实验结果
- 对多种领先基础模型和商业API（如Azure、Chirp 3、ElevenLabs、Meta OmniASR、Qwen3-ASR、GPT-4o Transcribe、Gemini等）进行了评估。
- 在低资源语言模块中，最佳WER/CER从9.63%（越南语）到51.34%（摩洛哥阿拉伯语）不等，远高于常见基准（如Common Voice中最佳WER/CER为1.50%-18.84%）。
- 在英语口音模块中，最佳WER从7.04%（中文口音）到23.68%（苏格兰口音）不等。
- 现有基准上的强性能无法可靠迁移到这些挑战性设置，暴露了评估盲点。

## 一句话评价
GigaSpeechBench是一个全面、真实、多语言多维度ASR/AST基准，填补了对中东、东南亚低资源语言、方言、口音、术语和年龄变化评估的空白，并证明了现有模型在真实场景中性能显著下降。

---

## 8. CTC-Seeded Token Edit Refinement for Non-Autoregressive Speech Recognition

**作者**: Wanting Huang, Weiran Wang
**链接**: [2606.28732](https://arxiv.org/abs/2606.28732)
**分类**: Speech Recognition | **关键词**: Non-autoregressive decoding, Diffusion model, Edit Flow, CTC confidence guidance, Classifier-free guidance, End-to-end ASR

## 核心痛点
传统非自回归语音识别（NAR ASR）方法通常从随机、完全掩码或固定长度标记序列开始，需要多次迭代重建完整转录，效率低下。CTC提供的贪婪假设虽然快速但精度有限，且现有扩散模型从无信息状态开始，浪费计算资源。

## 方法创新
1. **CTC初始化编辑细化**：将ASR解码公式化为对贪婪CTC假设的变长编辑细化（插入、删除、替换），利用CTC的强初始假设，仅需少量并行编辑步骤。
2. **声学条件编辑流解码器**：基于Edit Flow框架，直接操作折叠后的CTC标记序列，预测编辑操作和标记分布，实现变长序列并行编辑，无需填充或长度预测。
3. **连续时间离散扩散训练**：联合训练CTC和编辑流解码器，使用Levenshtein对齐定义编辑路径，损失函数包含CTC损失和编辑流扩散损失。
4. **推理策略优化**：使用CTC置信度门控编辑提案，结合分类器自由引导（CFG）聚焦声学特征，仅需2次编辑迭代即可显著降低WER。
5. **文本预训练**：在纯文本数据上通过删除、替换、插入噪声预训练编辑流解码器，为ASR训练提供强初始化。

## 实验结果
在LibriSpeech数据集上，使用ESPnet编码器时，test-clean/test-other的WER从3.5/7.9降至2.6/5.8（相对降低25.7%/26.6%）；使用Whisper medium编码器时，从2.6/6.1降至2.0/4.7（相对降低23.1%/23.0%）。消融实验验证了各设计选择的有效性，解码器预训练和预训练编码器集成带来显著性能提升。

## 一句话评价
该工作通过将NAR ASR重构为基于CTC假设的编辑细化，结合编辑流和扩散框架，以极小计算开销实现了卓越的识别精度提升。

---

## 9. Improving Large-Scale Weakly Supervised ASR by Filtering and Selection

**作者**: Kohei Matsuura, Masato Mimura
**链接**: [2606.28728](https://arxiv.org/abs/2606.28728)
**分类**: Automatic Speech Recognition | **关键词**: end-to-end automatic speech recognition, large-scale weakly supervised pretraining, data filtering, data selection, connectionist temporal classification

## 核心痛点
大规模弱监督ASR数据存在两个主要问题：1) 标签噪声（如拼写错误、未说话文本）；2) 数据多样性导致特定领域性能次优。传统方法通常只进行简单预训练，未充分处理这些问题。

## 方法创新
提出三步训练策略：
1. **Step 1: 预训练** — 使用整个弱监督数据集训练基于CTC的编码器-仅ASR模型。
2. **Step 2: 过滤与继续预训练** — 利用Step 1模型转录所有数据，计算字符错误率（CER），过滤掉CER高于阈值r的样本，然后继续预训练。
3. **Step 3: 数据选择与微调** — 若目标域训练集不可用，则从过滤后的子集中选择与目标域声学相似（基于SSL嵌入的余弦相似度）的样本进行微调。

关键创新点：将过滤和选择结合，且复用已用过的训练样本，不依赖额外数据。

## 实验结果
- 在90,000小时日语弱监督数据集上，过滤和选择分别协同降低CER达6.4%和4.0%。
- 过滤阈值r存在最优值，过低会丢失难样本，过高则保留噪声。
- 微调后改进趋势仍保持，表明方法广泛适用。

## 一句话评价
提出了一种简单有效的过滤与选择策略，显著提升了大规模弱监督ASR在目标域的性能，且无需额外数据。

---

## 10. OLIVE: View-Augmented Latent Prediction with Waveform Reconstruction for Speech SSL

**作者**: Karl El Hajal, Mathew Magimai.-Doss
**链接**: [2606.30356](https://arxiv.org/abs/2606.30356)
**分类**: Self-Supervised Speech Representation Learning | **关键词**: self-supervised learning, speech representation learning, view augmentation, masked prediction, waveform reconstruction, analysis-synthesis, invariant representation

## 核心痛点
现有语音自监督学习（SSL）方法主要专注于判别式任务（如ASR、说话人识别），通过对比预测、掩码建模等方式提取鲁棒的上下文表示，但缺乏对语音信号生成信息的保留，导致在生成任务（如波形重建、语音转换）上表现不足。传统的分析-合成范式在经典信号处理中有效，但在现代SSL中合成目标常被忽略或仅作为后处理。

## 方法创新
OLIVE提出联合优化分析和合成目标的端到端预训练框架：
- **分析分支**：基于视图增强的掩码蒸馏（view-augmented masked distillation）。对输入波形施加独立的数据增强（如时域变换），分别作为学生和教师视图，学生从掩码学生特征预测教师连续目标（归一化的多层教师输出均值的指数滑动平均），使用L2损失。
- **合成分支**：基于波形重建。使用HiFi-GAN生成器从早期编码器局部特征（未掩码的学生视图）重建波形，结合mel谱损失、对抗损失和特征匹配损失。
- **统一目标**：分析损失和加权合成损失联合优化，早期特征通过合成约束保留信号细节，后期上下文表示通过分析目标趋向不变性。解码器在预训练后保留，可直接用于波形生成。

## 实验结果（根据摘要推断）
OLIVE在生成任务和说话人相关任务上优于基线（如wav2vec 2.0、HuBERT、data2vec），在识别和语义任务上保持竞争力，并显著提升波形重建质量。

## 一句话评价
OLIVE通过统一的视图增强掩码预测与波形重建，首次在语音SSL预训练中实现了分析与合成的联合优化，平衡了判别性与生成性，为多任务通用表示学习提供了新思路。

---

## 11. Forewarned is Forearmed: When Non-Sequential Embedding Turns Into an Anomaly Detector

**作者**: Elys Allesiardo, Antoine Caubrière, Valentin Vielzeuf
**链接**: [2606.30196](https://arxiv.org/abs/2606.30196)
**分类**: Sentence Embedding Analysis | **关键词**: SONAR, multimodal, embeddings analysis, self-consistency, anomaly detection

## 核心痛点
SONAR等非序列化句子级嵌入模型在大规模多模态应用中虽有高效优势，但存在解码不稳定性，表现为输出中随机模式无限重复、句子截断等异常行为。这些异常类似于LLM的结构性幻觉，传统检测方法需内部解码概率或多次采样，计算成本高。

## 方法创新
本文提出一种基于嵌入自一致性的异常检测方法：计算原始语音嵌入与错误转录文本嵌入之间的余弦距离或欧氏距离，距离超过阈值则判定为异常。核心发现是异常转录的嵌入会远离原始嵌入。此外，通过分析每个维度对输入变化（速度、音高、词序、时长）的响应，识别出特定维度（如第654维）与输出长度相关，可用于异常修正。

## 实验结果
- 嵌入鲁棒性：速度0.5x/2x或音高±9半音时偏差大，但自然范围（0.75x-1.25x, ±3半音）内鲁棒。
- 词序扰动：n-gram洗牌降低解码质量，1-gram洗牌导致WER 87.9%，BERTScore 0.816。
- 说话人与音高探测：说话人识别准确率仅0.026（随机33倍），音高预测误差~79Hz，表明嵌入几乎不含说话人信息。
- 时长影响：第654维与输出长度强相关，修改该维度可控制输出长度，但仍存在异常。
- 异常检测：在LibriSpeech子集上，所提一致性检测器在适当阈值下精确率和召回率均优于BERTScore基线。

## 一句话评价
该工作揭示了非序列化嵌入维度可指示解码异常，并据此构建了高效、无需额外解码状态的检测器，为多模态概念模型的可靠性提供了新视角。

---

## 12. Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs

**作者**: Nithin Rao Koluguri, Sasha Meister, Nikolay Karpov, Piotr Zelasko, Desh Raj, Jagadeesh Balam, Boris Ginsburg
**链接**: [2606.29534](https://arxiv.org/abs/2606.29534)
**分类**: Automatic Speech Recognition Evaluation / ASR Benchmark | **关键词**: preference-aware evaluation, instruction-following, speech language models, automatic speech recognition, ASR benchmark

## 核心痛点
现有ASR测试集在数字、不流利、实体和大小写等格式上采用不一致的标注约定，标准归一化器抹去了用户关心的格式差异。当前基准无法衡量模型是否遵循用户对输出风格的偏好。

## 方法创新
- **Preference-ASR数据集**：包含3,210个（音频、指令、参考）三元组，覆盖四个偏好类别（归一化、实体、不流利、大小写），来自7个开源语料库。
- **两阶段LLM辅助构建管道**：第一阶段用Qwen3-30B-A3B对样本进行偏好分类；第二阶段生成指令和对应的偏好参考文本，经过人工验证。
- **偏好感知归一化器**：选择性跳过与活动指令匹配的归一化步骤，实现跨不同格式要求的公平WER计算。

## 实验结果
对四个模型（SALMONN、Qwen-Audio、Qwen2.5-Omni等）的基准测试显示，排名随偏好类型发生变化，暴露了传统评估掩盖的质量差异。

## 一句话评价
Preference-ASR通过条件化参考于用户指令，首次实现了对ASR系统遵循格式化偏好能力的系统评估，弥补了现有基准的空白。

---

## 13. An Optimal Contact-Mechanically Consistent and Flow-Separation Adapted Modeling of Vocal Fold Dynamics

**作者**: Sardar Nafis Bin Ali, Maryam Naghibolhosseini, Mohsen Zayernouri
**链接**: [2606.29071](https://arxiv.org/abs/2606.29071)
**分类**: Voice Biomechanics | **关键词**: Phonation Dynamics, Contact Mechanics, Flow Separation Force, Vocal Fold Closure, Lumped-Element Model, Particle Swarm Optimization

## 核心痛点
现有的单自由度（1-DOF）集总模型无法在结构阻尼下维持自激振动，除非引入复杂的声道耦合模拟；同时，这些模型难以准确模拟声带闭合阶段，常导致闭合不充分或物理不一致。多自由度模型虽能捕捉更多动力学特征，但参数多、计算开销大。

## 方法创新
1. **流分离补偿力**：通过额外阻力补偿流分离效应，在关闭阶段产生力不对称，实现自持振动，无需声道耦合。
2. **结构接触力**：在闭合阶段引入外部结构力，模拟声带碰撞，维持物理一致的闭合行为。
3. **参数优化**：利用高速视频内镜（HSV）数据，经深度学习分割提取声门面积波形（GAW），采用粒子群优化（PSO）算法最小化实验与模拟GAW的误差，获得个体化最优参数。
4. **数值求解**：采用四阶Runge-Kutta法增强稳定性和精度。

## 实验结果
- 对4名正常发音者（2男2女）的/i/音数据进行优化，归一化误差<3%。
- 模型成功复现个体化的声带振动模式及闭合特征，与实验数据吻合。

## 一句话评价
该研究提出了一种物理驱动、参数精简的1-DOF声带模型，通过流分离和接触力的显式建模，在不借助声道耦合的情况下实现了自持振动与准确闭合，为高效发声模拟提供了新范式。

---

## 14. Underwater Source Detection and Classification for Signal-based Surveillance: Audio Dataset Curation and Cross-Domain Evaluation

**作者**: Quoc Thinh Vo, David K. Han
**链接**: [2606.28988](https://arxiv.org/abs/2606.28988)
**分类**: Audio Dataset Curation and Cross-Domain Evaluation for Underwater Acoustics | **关键词**: Underwater acoustics, Audio dataset, Cross-domain evaluation, Class imbalance, Domain adaptation, Convolutional neural network

## 核心痛点
水下声学机器学习面临公开标记数据集稀缺的问题，与空气声学领域（如ESC50、GTZAN等大型基准）相比，水下数据集通常规模小、声学多样性有限，导致模型训练受限且跨域泛化能力差。此外，水下录音常包含重叠的生物和人为声音、强背景噪声以及类别不平衡，缺乏标准化的预处理和标注流程，限制了可重复性和公平基准比较。

## 方法创新
1. **数据集构建**：从开源海洋声音档案中手工筛选和分割，得到USS8数据集（1099个1秒片段，8个声学类别，最大最小类别不平衡比5.25）。
2. **基线模型**：使用轻量级Tiny-CNN，基于对数梅尔频谱图进行分类，域内准确率96.35%。
3. **损失函数改进**：提出margin-enhanced loss（CE-PlusPairMargin），在类加权交叉熵基础上加入logit间隔约束（如对船舶类强制其logit与鲸鱼、声纳类保持间隔），缓解类别不平衡和相似类别混淆。
4. **域适应策略**：在推理时使用特征统计对齐（特征均值和方差适配），并结合源域和目标域特征插值，提升跨域性能。

## 实验结果
- 域内测试：Tiny-CNN基线整体准确率96.35%，大多数类别F1超过0.92。
- 跨域零样本测试（ShipsEar）：标准交叉熵模型船舶检测率仅5.91%，而所提方法（CE-PlusPairMargin+特征对齐）将船舶检测率提升42.60%（从5.91%到具体数值？文中未明确给出提升后数值，但摘要称提升42.60%），显示更强的鲁棒性。

## 一句话评价
该工作通过构建新数据集和提出结合边际损失与特征对齐的方法，有效缓解了水下声学分类中的类不平衡和跨域漂移问题。

---

