# Arxiv Daily Deep Report - 2026-10-02

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 24
---

## 1. Multi-sample Synthetic Supervision for Accent Conversion

**作者**: Yangyang Qu, Michele Panariello, Massimiliano Todisco, Nicholas Evans
**链接**: [2610.01961](https://arxiv.org/abs/2610.01961)
**分类**: Accent Conversion | **关键词**: Accent Conversion, Multi-sample Supervision, Synthetic Supervision, Stochastic Generation, Target-accent Conditioning, Discrete Speech Tokens

# Multi-sample Synthetic Supervision for Accent Conversion 论文总结

## 核心痛点
- 口音转换（AC）要在改变口音的同时保留说话人身份和语言内容，但同一说话人、同一内容、不同口音的平行录音稀缺。
- 现有方法借助语音合成、迁移表示、离散语音 token、可控生成器（如 Vevo/Vevo2）构造监督，但生成过程具有随机性；同一源-口音条件下不同候选在目标口音实现和源保留质量上存在差异。
- 仅使用单个生成目标可能不足以提供高质量监督；且 AC 候选评估不能只看转录正确性，还需同时考虑目标口音、内容保留、说话人保留和时长一致性。

## 方法创新
- 将合成 AC 监督形式化为多样本目标构建问题：对每个源-口音条件生成多个波形-离散 token 候选，联合评估目标口音实现与源保留，再将波形级选择结果转移到配对的 content-style token 序列上作为伪监督。
- 两阶段框架：Stage 1 先利用参考条件生成构造 token 级目标，训练分类口音条件自回归生成器 G_phi；该生成器使用 32 个可训练口音嵌入和共享 rank-32 LoRA 适配 query/key/value/output 投影，其余骨干冻结。固定 G_phi 后，对每个源转录 t 和目标口音 a 采样 N=8 个 content-style token 序列，并用冻结 Flow Matching + Vocos 结合源波形 x 合成候选波形。
- 候选评估与选择：联合检查目标口音证据、WER、说话人相似度、时长比例；满足 τ_WER、τ_SIM、时长范围和口音预测条件后，按 p_i、Δp_i、h_i、s_i 降序及 w_i 升序进行字典序选择。选中波形对应的 token 序列 z* 用作最终监督。
- Stage 2 训练最终转换器 p_theta：采用与 G_phi 相同的分类自回归架构，从种子特定热启动初始化，仅优化口音嵌入和共享 LoRA，最小化选中 token 序列的因果 token 负对数似然。推理时仅需 (t, x, a)，生成单个 token 序列后经冻结声学合成得到转换波形，无需目标口音参考语音、多候选生成或候选选择。
- 通过受控比较单样本 vs 八样本监督，保持源-口音群体、数据划分、每个种子初始化和优化协议一致，以隔离“从多个随机实现中选择目标”带来的下游效果。

## 实验结果
- 与每个训练示例使用一个生成目标相比，八样本监督将目标口音分类准确率提高 2.49 个百分点；说话人相似度几乎不变；WER 增加 0.29 个百分点。
- 在六个英语目标口音（阿拉伯语、中文、印地语、韩语、西班牙语、越南语）上，方法达到 7.81% WER，并在所评估系统中获得最高平均听力评分。
- 实验数据规模：29,754 个源-口音条件来自 LibriTTS（17,649 话语、235 说话者）和 L2-ARCTIC（12,105 话语、20 说话者），每个口音 4,959 个条件。G_phi 先用 29,840 个伪目标 token 序列适配。
- 多样本构建设置：N=8，top-k=25，top-p=0.8，temperature=1.0，32 步 Flow Matching；过滤阈值 τ_WER=0.08、τ_SIM=0.60、ρ∈[0.75,1.45]、τ_Δ=0.02；16,153 个条件至少有一个可行候选，划分 15,346 个优化条件和 807 个内部验证条件，另有 300 条件开发集用于检查点选择。

## 一句话评价
该论文把口音转换的合成监督从“单目标”推进为“多随机样本联合评估与选择”，在不显著损害说话人相似度和 WER 的前提下提升目标口音准确性，为稀缺平行数据下的 AC 训练提供了有效的多候选监督范式。

---

## 2. Shared-State Local Translations for Training-Free Voice Conversion

**作者**: Yangyang Qu, Michele Panariello, Massimiliano Todisco, Nicholas Evans
**链接**: [2610.01952](https://arxiv.org/abs/2610.01952)
**分类**: Voice Conversion | **关键词**: Voice Conversion, Training-Free, Self-Supervised Speech Representations, WavLM, Gaussian Mixture Model, One-Shot Voice Conversion

# Shared-State Local Translations for Training-Free Voice Conversion (StateVC)

## 核心痛点
- 一次性无训练语音转换中，源语音与参考语音的语言内容可能不同，因此不能假设可靠的帧级对应关系。
- 现有基于自监督表示的方法（kNN-VC、LinearVC、kDOT、MKL-VC、USCF、SSL-GMMVC 等）通常需要显式建立源-参考帧关系、做最近邻或最优传输配对，或者先配对再拟合 GMM。这些做法可能引入配对误差，并限制对局部源到参考变化的估计。
- 论文核心问题：能否在不预先配对源/参考帧的情况下，估计局部源到参考变化？

## 方法创新
- 提出 StateVC，一种无需训练的一次性语音转换方法，不需要训练或微调神经网络参数。
- 使用冻结的 WavLM 编码器提取源和参考的帧级表示。
- 共享状态定义：在按时间标准差排序选出的低维路由空间（dc=24）中，将源和参考帧拼接，拟合一个针对当前语音对的共享对角协方差 GMM。每个混合分量称为一个 state。通过 BIC 和最小分配帧数 nmin 选择状态数 Ke，无需源-参考帧匹配，也避免分别拟合 GMM 后的组件匹配问题。
- 状态分配：计算每帧对各个状态的后验概率作为 routing probability，并进行 L=5 帧时间平滑与归一化。
- 局部平移估计：在原始 D=1024 维 WavLM 空间中，用平滑后验权重计算每个状态的源/参考加权均值。若两个话语在某状态的后验质量均不低于 mmin，则该状态的源到参考 shift 为参考均值减源均值；否则回退到话语级均值差。
- 后验加权帧更新：对每个源帧，用其状态后验组合各状态 shift：H'_s[t] = H_s[t] + λ Σ_k γ_s(t,k) Δ*_k。λ 控制转换强度，不同帧可获得不同局部更新，称为 soft routing。
- 波形重建：使用冻结的 WavLM-conditioned HiFi-GAN（来自 kNN-VC）从更新后的表示合成语音。

## 实验结果
- 数据集与协议：LibriSpeech test-clean，按 MKL-VC 设置构建 7,800 个跨说话人 pair：40 个说话人，每个源说话人取 5 条源语音，与每个其他说话人的 1 条参考语音配对。
- 客观指标：SIM 为 SpeechBrain x-vector 余弦相似度；WER/CER 使用 Whisper-base 对源转录评测。
- 主观指标：20 名听者对相同 40 对源-参考进行 N-MOS（1–5 自然度）和 S-MOS（1–4 感知相似度）评分。
- 主要结果：StateVC 在评测系统中取得最低 WER 8.01% 和 CER 3.22%，SIM 0.9512；感知说话人相似度均值最高，并且在无训练系统中自然度均值最高。N-MOS 3.550，S-MOS 2.750。
- 对比基线：FreeVC、FreeVC-S、kNN-VC、LinearVC、MKL-VC、kDOT、USCF、SSL-GMMVC。MKL-VC 为 WER 8.22/CER 3.37；StateVC 略优且 SIM 更高。
- 消融与设计分析：
  - 共享 GMM 状态定义优于分离 GMM + Hungarian：共享 GMM 为 WER 8.44/CER 3.48；Hungarian 为 13.82/6.60；同索引为 40.28/26.40（Block 变换固定）。
  - soft routing 优于 hard routing；hard routing 只选择最可能状态的 Block 变换输出，soft routing 用源帧后验组合状态特定变换。
  - 比较 Mean、Diagonal、Block 三种状态特定变换，说明共享状态框架是否需要比均值平移更灵活。
  - 敏感性分析涵盖转换强度 λ、候选状态数上限 Kmax、参考语音时长对 SIM/WER 的影响。

## 一句话评价
StateVC 通过共享状态 GMM 与后验加权局部均值平移，在不做源-参考帧配对的前提下实现了高质量、无需训练的一次性语音转换，在内容保持和说话人相似度上取得有竞争力的结果，并在评测的无训练系统中表现突出。

---

## 3. Teaching LLMs to Hear Who Spoke What: Metadata-Supervised Pretraining for Encoder-Free Speech-LLMs

**作者**: Mohan Shi, Ruchao Fan, Sunit Sivasankaran, Keqi Deng, Jinyu Li
**链接**: [2610.01695](https://arxiv.org/abs/2610.01695)
**分类**: Speech-LLM | **关键词**: Encoder-free Speech-LLM, Metadata-supervised Pretraining, Speaker-aware Utterance Composition, Joint ASR and Diarization, Paralinguistic Understanding

## 核心痛点
现有基于编码器的 Speech-LLM 通常使用预训练语音编码器，这些编码器多以语义导向目标（如 ASR）优化，倾向于优先保留语言内容而丢弃细粒度声学线索（如说话人身份、情感等副语言信息）。已有双编码器或辅助目标等方法增加了架构或训练复杂度。近期无编码器 Speech-LLM（如 Gemma、Mel-LLM）直接将 Mel 频谱映射到 LLM 输入空间，但缺乏系统的预训练策略来弥补大规模预训练编码器的缺失，且不清楚其能否从低层声学特征中有效获取并保留说话人相关及副语言信息。

## 方法创新
1. **元数据监督预训练 (MSP)**：利用说话人身份、情感等语音属性作为监督信号，与转录任务联合预训练，促进说话人区分和副语言理解。
2. **说话人感知语句组合 (SAUC)**：在训练批次中动态拼接单说话人语句，模拟多人对话（含重叠和静音间隔），合成多说话人长语音，增强说话人区分能力。
3. **随机跨度掩码**：对输入特征进行跨度掩码正则化，以 12.5 Hz 分辨率定义，概率 p=0.04、长度 L=4（约 320 ms），期望掩码比例约 15%。
4. **无编码器架构**：基于 Phi-4-MM，80 维 log-Mel 频谱经轻量卷积下采样（r=8，12.5 Hz）和线性投影映射到 LLM 嵌入空间；LLM 冻结并用 LoRA 适配，仅更新前端、投影和 LoRA 参数。

## 实验结果
- 主要在**联合 ASR 和说话人日志**任务上评估，使用 AMI (IHM-Mix) 和 CH109 Full 测试集，指标为 WDER 和 cpWER。
- 在**匹配训练数据**条件下，无编码器模型整体优于随机初始化的编码器基线。
- 在**有限元数据标注数据**下，与使用大规模预训练语音编码器的模型相比具有竞争力，并在多个设置中超越。
- 在**副语言任务**（情感、年龄、性别识别、说话人验证）上也验证了有效性。

## 一句话评价
该工作首次系统研究了无编码器 Speech-LLM 的元数据监督预训练，通过 SAUC 和掩码策略显著提升了说话人区分和副语言理解能力，在联合 ASR 与说话人日志任务上达到与预训练编码器模型相当甚至更优的性能。

---

## 4. Code-Switching Spoken Language Identification as Multi-Label Set Prediction

**作者**: Shunsuke Mitsumori, Matthew Wiesner, Shigeo Morishima, Shinji Watanabe
**链接**: [2610.01450](https://arxiv.org/abs/2610.01450)
**分类**: Spoken Language Identification (Code-Switching) | **关键词**: Code-Switching Spoken Language Identification, Spoken Language Identification, Multi-Label Set Prediction, Code-Switching Speech, Language Set Generation

# 论文总结

**论文标题**：Code-Switching Spoken Language Identification as Multi-Label Set Prediction
**作者**：Shunsuke Mitsumori, Matthew Wiesner, Shigeo Morishima, Shinji Watanabe（Waseda University / Johns Hopkins University / Carnegie Mellon University）

## 核心痛点
1. **单语LID过滤泄露CS语音**：从网络爬取的大规模多语语音语料在预处理时依赖话语级LID，但即使经过YODAS/OWSM v4等严格筛选，仍混入code-switched（CS）语音。问题不在CS本身，而在于单语标签与多语内容不匹配，会偏置语言平衡采样、污染语言特定评测、向语言条件ASR训练中泄露非目标语言。
2. **现有话语级CS-LID范式局限**：一类方法把每个CS语言对视为原子类别（如jpn-eng），兼容多分类LID，但忽略CS的组合性，无法处理训练中未见的语言对；随语言库存增大，可能语言对数量二次增长，为每个语言对收集CS数据不现实。另一类方法保留单语言输出库存，从LID分数导出语言集合，如Top-k或阈值解码。Top-k需要预言机语言数k，阈值解码不需要k但性能依赖工作点，跨语言、领域和CS密度不稳定。
3. **核心目标**：实现CS-aware LID，能够识别每个话语中出现的语言集合，并泛化到未见语言组合。

## 方法创新
- **任务重构**：将话语级CS-LID形式化为多标签语言集合预测（multi-label language-set prediction），输出语言集合如{jpn, eng}，而非原子对标签jpn-eng。
- **集合生成器（set generator）**：直接生成语言token序列，再转换为无序语言集合，并过滤到已知语言库存L内。生成<jpn>得到{jpn}，生成<jpn><eng>得到{jpn, eng}。模型同时预测语言数量与具体语言：预测数量k̂=|Ŷ(x)|；k̂=1视为单语，k̂≥2视为CS。该方法避免原子对标签、预言机语言数k和手工阈值，并让未见语言对表现为已知语言的新组合。
- **对比基线**：
  1. 硬目标多分类 + 原子对标签（C_atomic = L ∪ {[ℓ_a, ℓ_b]}）；
  2. 软目标softmax分类，CS话语使用等质量目标分布(1/|Y(x)|)，用KL散度优化；
  3. sigmoid多标签分类，使用multi-hot目标和BCE损失；
  4. 多标签语言集合生成。
- **模型架构**：所有系统共享965M参数MMS-1B前端并参与更新，多层表示通过可学习加权和组合并在话语级归一化。分类器基于ESPnet LID recipe，经ECAPA-TDNN编码器、channel-attentive statistics pooling、RawNet3风格投影器得到话语嵌入，再接subcenter cosine head（K=3, m=0.5, s=30）。可训练参数除MMS-1B外分别为9.33M/9.32M/9.32M/23.55M。训练3 epoch，有效batch size 32，学习率线性预热3e-6到5e-6等。

## 实验结果
- **数据集**：FLEURS（102语言单语LID训练/评测）、CS-FLEURS（Read、XTTS1、XTTS2、MMS测试子集；XTTS1全为已见语言对，XTTS2全为未见语言对；Read/MMS含已见与未见）、CS-YODAS（训练，英语与阿拉伯语、汉语、法语、印地语、日语、俄语等自然CS语音）、Bangor Miami Corpus（西班牙语-英语，评测英语占比变化）、Multilingual Soap Opera Corpus（英语、isiXhosa、isiZulu三语CS评测）。
- **主要发现**：
  - Oracle Top-k是最强基线；但阈值法失败，因为不存在单一阈值能区分CS与单语语音。
  - 原子对分类在已见语言对上表现好，但结构上无法预测未见语言对。
  - 基于分数的分类（softmax/sigmoid）配合Top-k是很强的oracle-cardinality基线，阈值解码准确率不及Top-k。
  - 集合生成器能在未见语言对上预测正确的语言数量，且不假设语言数；但在精确集合准确率上仍低于Oracle Top-k。
  - 论文指出稳健CS-LID的关键障碍：oracle cardinality（预言机语言数依赖）、阈值不稳定性、CS训练数据中的语言偏置、合成到真实的域差（synthetic-to-real gap）。
- **结论**：多标签集合生成避免了原子对标签、预言机语言数和手工阈值，但尚未超越Top-k基线；面向未见、非英语和真实世界CS语音的稳健语言集合预测仍是开放挑战。代码在ESPnet cs-fleurs recipe开源。

## 一句话评价
该论文将CS-LID从“原子语言对分类”或“依赖oracle k/阈值的分数解码”推进到多标签语言集合预测，思路清晰且系统对比充分，但当前集合生成器仍未在精确集合准确率上超越Oracle Top-k，说明鲁棒CS-LID仍需解决语言数预测、阈值稳定性和合成-真实域差等核心问题。

---

## 5. PADP: Perceptual Audio Data Perturbation for Probing Perception Awareness in Audio Quality Models

**作者**: Guanxin Jiang, Andreas Brendel, Pablo M. Delgado, Jürgen Herre
**链接**: [2610.01405](https://arxiv.org/abs/2610.01405)
**分类**: Audio Quality Assessment | **关键词**: Perceptual Audio Data Perturbation, Audio Quality Assessment, Psychoacoustics, Objective Audio Quality Metrics, Foundation Models, MUSHRA

## 论文信息
- 标题：PADP: Perceptual Audio Data Perturbation for Probing Perception Awareness in Audio Quality Models
- 作者：Guanxin Jiang, Andreas Brendel, Pablo M. Delgado, Jürgen Herre
- 机构：International Audio Laboratories Erlangen, Fraunhofer IIS
- 领域：感知音频质量、心理声学、音频扰动、客观音频质量度量、基础模型

## 核心痛点
- 人类听觉系统是选择性提取感知相关信息的复杂过程，对某些细粒度信号变化不敏感。
- 现有客观音频质量模型（包括感知驱动模型和基于学习的模型）是否以与人类感知一致的方式评估音频质量尚不明确。
- 若模型要密切反映人类判断，应对感知上不相关的信号修改保持不敏感，但缺乏系统性的压力测试。
- 已有心理声学约束的对抗扰动多依赖掩蔽原则，且缺少严格的主观透明性验证。

## 方法创新：PADP
提出 Perceptual Audio Data Perturbation (PADP)，一组引入感知不相关失真的音频变换，作为音频质量模型的鲁棒性探针。包含四种变换：
1. APX (All-Pass Band Phase-Shift Combination)：基于听觉频率选择性和对相位修改的有限敏感性，在 QMF 感知频带上分组施加相位旋转，保持频谱幅度。
2. DEL (Frequency-Selective Delay)：基于听觉频率依赖的时间分辨率，对选定感知频带施加固定延迟模板，通常低频延迟更大。
3. SCD (Scaled Coding Distortion)：利用高质量编解码重建作为感知可忽略加性噪声，通过线性插值 x'=(1-λ)x+λx_r 控制扰动强度。
4. DIF (Decorrelator/Diffusion)：基于 MPEG Surround 全通去相关，通过 ICC 控制空间扩散，混合直接与去相关分量，保持音色。
实现基于 MPEG Surround QMF 滤波器组（F=64，f=23 感知频带），使用固定二进制映射矩阵 G 将感知频带映射到 QMF 子带，并支持近无混叠重建。

## 实验设计
- 不可听性验证：从 Open Dataset of Audio Quality (ODAQ) 选取 12 个干净信号，覆盖平均与关键项目；采用 MUSHRA 听音测试（两个测试分别 6 和 7 个条件），含隐藏参考和 3.5 kHz 低通锚；后筛选后分别保留 9 和 8 名听众。参数设置：APX 采用 o=1, s=4, α=π/2；DIF 采用 d=1,3,5；SCD 使用 mp3 80 kbps 和 λ∈{0.2,0.6,0.9,1.2}；DEL 使用固定延迟模板。
- 模型鲁棒性评估：评估 4 个感知驱动模型（PEAQ Basic、2f-model、ViSQOL v3、HAAQI）、2 个学习型模型（SCOREQ、DeePAQ）和 4 个音频基础模型（MERT、MuQ、CLAP、wav2vec 2.0）。对不直接输出全参考质量分数的模型，使用参考与变换信号嵌入的欧氏距离，并与主观评分比较。
- 透明性准则：差异等级（隐藏参考与项目等级之差）小于 10 视为透明。

## 实验结果与结论
- 听音测试用于验证 PADP 变换达到透明或近透明质量，确保感知不相关。
- 模型评估显示：这些感知等效变换可挑战 SOTA 音频质量评估系统和基础模型，暴露模型响应与人类感知判断之间的不一致。
- 结论：当前模型对某些 PADP 变换缺乏感知意识，说明其鲁棒性和感知对齐性有限。
- 提供的片段截断，完整定量结果（各模型分数、统计显著性等）未包含在给定内容中。

## 一句话评价
PADP 通过心理声学启发且经主观验证的感知不相关扰动，系统性地揭示了客观音频质量模型与人类听觉感知之间的错位，为评估和提升音频质量模型的感知鲁棒性提供了新工具。

---

## 6. A Federated Deepfake Speech Detection Method Based on Layer-Wise Center-Guided Weighting Aggregation

**作者**: Yingjian Yu, Haiyan Guo, Tianshun Wang, Zirui Ge, Chi Liu
**链接**: [2610.01259](https://arxiv.org/abs/2610.01259)
**分类**: Deepfake Speech Detection / Federated Learning | **关键词**: deepfake speech detection, federated learning, layer-wise aggregation, FedProx, model aggregation

## 核心痛点

深度学习语音合成技术的飞速发展（尤其是基于 Audio Language Model 的 TTS 系统）使得深度伪造语音的多样性和逼真度大幅提升，对声纹认证等语音系统安全构成严重威胁。现有 DSD 方法存在两大问题：

1. **域偏差与检测失效**：主流检测模型（RawNet2、ASSIST、W2V2、WavLM、Mamba 等）多基于声码器合成数据训练，难以检测新兴 ALM-based TTS 生成的伪造语音；虽然 Codecfake 数据集与集中式 co-training 策略可缓解该问题，但需要强大的中心服务器与海量存储/算力，资源受限客户端无法承担。
2. **隐私风险**：客户端持续产生新语音数据，若想持续受益于 co-training，需上传原始语音，而原始语音含敏感个人信息，存在严重隐私泄露风险，且用户往往不愿或不被法律允许共享。

## 方法创新

论文提出 **FedDSD（Federated Deepfake Speech Detection）**，利用联邦学习在不上传原始音频的前提下协同训练全局 DSD 模型，主要贡献包括：

- **FedProx 本地训练**：针对客户端数据异构导致的 client drift，在本地目标函数中引入近端项 \(\frac{\mu}{2}\|w_k - w_G\|^2\)，约束本地参数偏离全局模型，提升异构数据下的训练稳定性与收敛性。
- **L-CGWA 分层中心引导加权聚合（Layer-wise Center-Guided Weighting Aggregation）**：
  - 针对不同客户端在对应层上表征失配、且不同层受异构影响程度不同（浅层学通用声学模式、深层对数据集特有特征更敏感）的问题，在每一层单独聚合。
  - 以所有客户端该层参数的算术平均 \(w^t_{center,l}\) 作为参考中心，权重取客户端该层参数到中心距离的倒数（加 \(\epsilon\) 平滑），即 \(\tilde{\alpha}^t_{k,l} = 1/(\|w^t_{k,l}-w^t_{center,l}\|_2+\epsilon)\)，再归一化。
  - 效果：越接近共识中心的更新获得越高权重，偏离较大的异常/过度特化更新被抑制，无需显式离群点检测即可增强聚合鲁棒性，并比传统均匀权重聚合更灵活自适应。
- **框架流程**：全局模型下发 → 本地更新（FedProx）→ 本地模型上传 → L-CGWA 聚合，兼顾隐私保护与资源受限客户端受益。

## 实验结果

- 在 FedDSD 下训练的模型，其等错误率（EER）与集中式 co-training 方法相当；
- 显著优于在单个数据集上孤立训练的模型；
- 在跨域数据集上展现出强泛化能力；
- 为验证通用性，本地模型选用 W2V2-AASIST 与 RawBMamba 两种架构。

## 一句话评价

本文首次系统性地将联邦学习引入深度伪造语音检测，通过 FedProx 缓解数据异构并创新性地提出分层中心引导加权聚合（L-CGWA），在保护语音隐私的同时达到接近集中式 co-training 的检测性能与跨域泛化能力，为隐私约束下的 DSD 协作训练提供了有效方案。

---

## 7. FedCFM: Federated Continual Domain Generalization for Fake Speech Detection via Conditional Flow Matching

**作者**: Yingjian Yu, Haiyan Guo, Tianshun Wang, Xinzhou Xu, Zirui Ge, Chi Liu, Ziheng Liu
**链接**: [2610.01242](https://arxiv.org/abs/2610.01242)
**分类**: Fake Speech Detection (Audio Anti-Spoofing) | **关键词**: Fake Speech Detection, Federated Domain Generalization, Conditional Flow Matching, Continual Learning, Generative Replay

# FedCFM: Federated Continual Domain Generalization for Fake Speech Detection via Conditional Flow Matching

## 核心痛点
- **FSD模型泛化能力对实际部署至关重要**，但现有方法多依赖固定训练集，难以适应持续出现的新型伪造攻击。
- **持续学习虽被探索，但许多方法忽略单个设备存储有限**，导致实际可用性受限。
- 真实场景中，语音数据分布在机构、平台或边缘设备上，不同客户端观测到的伪造源高度异构；**原始语音共享受隐私与所有权限制**，难以集中训练。
- 因此，如何在**不共享原始语音数据**的前提下，实现分布式客户端间持续、可泛化的伪造语音检测协作，仍是一个开放问题。

## 方法创新
- 提出 **FedCFM**：一种基于**条件流匹配（CFM）**的联邦持续域泛化框架，面向伪造语音检测。
- 每个客户端训练一个 **CFM 生成器**，显式建模**伪造类型特定的嵌入分布**；客户端间交换生成器而非原始语音或可直接观察的语音数据，实现模型级分布知识共享。
- 服务器收集并重分发客户端私有生成器；各客户端利用其他客户端生成器合成**本地缺失攻击类型的嵌入**，用于持续分类器更新。
- 分类器同时使用**本地观测嵌入**与**合成嵌入**训练，更新后的分类器参数在服务器端通过 FedAvg 聚合成全局模型。
- CFM 生成器采用轻量级 Matcha-TTS 变体，以**线性注意力模块替代 Transformer 块**，降低联邦学习约束下的模型复杂度。
- 训练目标联合 **CFM 速度场回归损失**与**监督对比损失（SupCon）**，促进同伪造类型嵌入紧凑、不同伪造类型嵌入分离，增强条件判别性与类条件分布建模。
- 支持持续/域增量场景：新语音数据按间隔到达，客户端更新生成器并持续适应新兴攻击，同时通过生成重放与知识蒸馏/参数聚合保留历史知识。

## 实验结果
- 在相同训练数据集下，**FedCFM 的 EER 低于所评估的集中式和联邦域泛化基线**，表现出较强的跨域泛化能力。
- 表 I 汇报了多种代表性域泛化方法在多个测试集上的 EER（%），测试集包括 19LA、CFAD、ASV5、CF、SF、21LA、21DF、ITW、ADD22、AI4T、SONAR、CD-ADD 等。
- 对比方法包括单数据集训练基线，如 XLSR-MOE、VV-SSLD、XLSR-AASIST、Fake-Mamba 等；FedCFM 在相同训练集设定下取得更优结果。
- 代码将发布于：https://github.com/jspycpp/FedCFM。

## 一句话评价
FedCFM 将条件流匹配生成器引入联邦持续域泛化，用“生成器交换”替代原始语音共享，为隐私约束下持续演化伪造攻击的鲁棒检测提供了一种有前景的协作学习范式。

---

## 8. ParaCalib: Semantically Calibrated Paralinguistic Modeling for Depression Detection

**作者**: Yuxin Li, Yifei Li, Yi-Wen Chao, Xiangyu Zhang, Eng Siong Chng, Cuntai Guan
**链接**: [2610.01103](https://arxiv.org/abs/2610.01103)
**分类**: Speech-based Depression Detection | **关键词**: Depression Detection, Paralinguistic Modeling, Semantic Calibration, Audio-Language Model, Multiple Instance Learning, SC-Para

## 核心痛点
- 现有语音抑郁检测大多遵循**声学标记范式**：将声学线索视为与上下文无关的抑郁标记，直接映射为参与者级证据。
- 这一范式忽略了一个关键问题：**同一语音形式在不同语义上下文和交际功能下可能有不同解释**。例如长停顿、平坦音高、低能量或语速变化，既可能反映抑郁性精神运动变化，也可能来自犹豫、强调、句法规划、话轮转换或表达内容本身。
- 抑郁本身具有临床异质性：可能表现为精神运动迟滞，也可能表现为激越，因此抑郁相关语音并不存在单一、统一的声学轮廓。
- 现有 ALM 方法虽能生成丰富的自由文本描述，但自由文本难以跨话语和参与者稳定比较；封闭集情感分类又过于粗粒度，压缩了副语言差异。

## 方法创新
- 提出 **ParaCalib**：一个通过语义校准副语言行为进行抑郁检测的框架。其核心定义是：相对于话语级语义上下文和推断出的交际功能来解释语音行为，并将其表示到结构化、可比较的状态空间中。
- 整体流程包括三阶段：
  1. **ALM 语音描述生成**：使用冻结的 **Qwen3-Omni-30B-A3B Captioner**，对每个话语级音频片段生成自然语言语音描述，同时捕捉“说了什么”和“怎么说”。
  2. **PSE 提取 SC-Para 表示**：使用冻结的 **DeepSeek-R1-Distill-Qwen-32B** 作为 Paralinguistic State Extractor，将自由文本描述映射为固定维度的 **Semantically Calibrated Paralinguistic (SC-Para)** 向量。
  3. **注意力 MIL 聚合**：对每个参与者，将有效话语级 SC-Para 向量组成实例包，使用注意力机制估计实例权重，并以原始 7 维 SC-Para 向量的加权和形成参与者级表示，最后输入 MLP 进行抑郁标签预测。
- **SC-Para 表示包含 7 维**：
  - 5 个组成维度：音高变化性、语速、节奏规律性、停顿模式、声音能量；每个维度取 0/1/2 三个离散状态。
  - 2 个整体维度：抑郁相关副语言证据分数（0–100 归一化到 [0,1]）和置信度分数（[0,1]）。
- 若 PSE 因描述中语音证据不足而将任一类别维度标为 unknown，则该话语在参与者级聚合前被排除。
- 训练时 ALM 和 PSE 均保持冻结，只优化下游 MIL 分类器，避免在数据集上微调，也避免使用参与者级抑郁标签。

## 实验结果
- 在 **DAIC-WOZ** 和 **MODMA** 数据集上，ParaCalib 在所评估方法中取得最高平均 **Macro-F1**：
  - DAIC-WOZ：**71.9%**
  - MODMA：**90.5%**
- 优于传统声学表示和 SSL 语音表示，同时提供可检查的中间副语言状态。
- **受控分析**：在固定 caption-level 声学描述的条件下，改变伴随的语义上下文会改变 PSE 推断出的抑郁相关副语言证据，直接证明语义校准在 PSE 阶段被 operationalized。
- **探索性分析**：发现与抑郁标签相关的重复性副语言状态配置，而不是单一均匀占主导的状态。

## 一句话评价
ParaCalib 通过“ALM 描述 + PSE 结构化映射 + 注意力 MIL 聚合”将副语言行为语义校准到可比状态空间，为语音抑郁检测提供了上下文敏感、可解释且具有组合性的新范式。

---

## 9. MAV-C: A Framework for the Joint Objective Estimation of Audio-Visual Complexity in Immersive Virtual Environments

**作者**: Luca Resti, Amelia Gully, Michael McLoughlin, Gavin Kearney, Alena Denisova
**链接**: [2610.00754](https://arxiv.org/abs/2610.00754)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 10. Articulatory Source-Filter TTS: Physically Grounded Control through Vocal Tract Kinematics

**作者**: Jesuraj Bandekar, Shinji Watanabe, Prasanta Kumar Ghosh
**链接**: [2610.00735](https://arxiv.org/abs/2610.00735)
**分类**: Text-to-Speech (Articulatory/Source-Filter TTS) | **关键词**: Articulatory Source-Filter TTS, Acoustic-to-Articulatory Inversion, Vocal Tract Kinematics, Optimal Transport Conditional Flow Matching, Interpretable Speech Synthesis, Accent Modification

## 核心痛点
- 现代神经 TTS 系统声学保真度与自然度很高，但通常作为黑盒运行，难以对物理语音产生过程提供可解释、细粒度的控制。
- 已有可控 TTS 多暴露音高（pitch）与能量（energy），或分离源与滤波器频谱，但声道滤波器仍缺少与发音运动学相对应的物理参数化，也未与成熟的语音产生理论直接连接。
- 实时 MRI（rtMRI）可捕捉完整发音数据，但成本高且存在声学混响；EMA 更可行但语料规模小。AAI 虽借助自监督学习表示和辅助任务预训练显著提升性能，但其伪发音轨迹多用于语音转换或编码，尚未系统集成到 TTS 中以实现滤波器物理接地。

## 方法创新
1. 提出一种可控 source-filter TTS 架构：滤波器响应由预测的发音轨迹显式条件化，声门源由预测的音高和能量轮廓参数化；源与滤波器独立预测，源再经 Optimal Transport Conditional Flow Matching（OT-CFM）模块细化，最后与滤波器重组为最终频谱图。作者称这是首个文本驱动、具有运动学级声道物理控制的 TTS。
2. 设计两阶段 AAI 伪标注管线：先在 EMA-语音平行数据上训练 Transformer 式 AAI 模型，采用大规模多语言预训练模型 MMS-1B 提取声学表示，并从不同深度提取表示以增强跨语言 AAI；模型预测 12 通道中矢状发音轨迹（唇、颌、舌）。随后在大规模 TTS 语料上生成发音伪轨迹，作为 TTS 训练中的滤波器条件监督，将发音监督从小规模 EMA 扩展到数百小时未配对 TTS 语音。
3. 显式源-滤波器解耦带来可控性：支持稳定的韵律缩放，以及跨说话人的源/滤波器交换与重组；在交换中，F0 等韵律源属性保持跟随源说话人，而声道频谱特征跟随滤波器说话人。
4. 支持可解释的发音层控制与口音修改：通过直接空间操作发音轨迹，例如压平舌尖和舌体手势，可将美式卷舌 /r/ 转为非卷舌实现，并在合成音频中观察到对应的 F3 偏移。

## 实验结果
- 合成语音的可懂度和自然度与同尺寸基线具有竞争力；由于输出被约束到显式源-滤波器分解，仅带来适度的频谱保真度代价，但换取了黑盒系统不具备的控制能力。
- 定量与定性评估显示显式源-滤波器解耦：源侧扰动（音高/能量缩放）时滤波器侧属性（共振峰、频谱包络）保持稳定；跨说话人交换时音高保持源说话人，频谱特性跟随滤波器说话人。
- 定性发音-声学分析表明，模型可在最小对中解耦不同发音器，并恢复后元音 /r/ 的典型美式卷舌姿态；还展示了通过发音轨迹空间操作实现口音修改等细粒度控制。
- 音频样本见项目页：https://coding-phoenix-12.github.io/ArticulatorySFTTS/。

## 一句话评价
该工作将 source-filter 语音产生分解与 AAI 发音运动学相结合，为 TTS 提供了物理接地的可解释声道控制，在源-滤波器解耦、跨说话人重组和发音层口音编辑方面具有潜力，但依赖 AAI 伪轨迹且以一定频谱保真度为代价。

---

## 11. Frequency-Weighted Soft-Constrained Spatially Selective Active Noise Control for Open-Fitting Hearables

**作者**: Tong Xiao, Reinhild Roden, Matthias Blau, Simon Doclo
**链接**: [2610.00721](https://arxiv.org/abs/2610.00721)
**分类**: Active Noise Control | **关键词**: Spatially selective active noise control, Soft-constrained SSANC, Frequency weighting, Open-fitting hearables, Speech enhancement, Low-delay time-domain processing

## 核心痛点
- 多说话人环境中，听者需要在干扰说话人和其他噪声存在时聆听目标说话人；hearables 可保留目标语音并衰减干扰声。
- 开放式耳戴设备降低堵耳效应、提升舒适度，但目标语音和干扰声都会通过声泄漏到达耳膜，传统空间滤波（MVDR/MPDR）未显式建模泄漏和次级路径；传统 ANC 会无差别衰减目标语音和噪声。
- 硬约束 SSANC 精确保持目标语音，但可能限制可实现的降噪量；软约束 SSANC 通过标量权衡参数在降噪和语音保持间折中，但仍为全频带统一权重。
- 多通道语音增强中的频率相关加权（SPP、心理声学掩蔽、SII 感知加权）通常采用块处理，可能不兼容 SSANC 低处理时延。

## 方法创新
- 提出频率加权软约束 SSANC：在低时延时域主动控制中，对目标语音保持误差施加频率加权滤波器 f，构造加权卷积矩阵 F。
- 优化问题：min_w E{e²(n)} + β||w||²₂ + μ||F[H(q+Gw)-δ_Δ]||²₂。其中 μ 控制整体语音保持与降噪权衡，F 控制不同频带的惩罚强度。
- 被加权强调的频带对目标语音保持误差惩罚更强，有利于语音保真；弱加权频带给降噪更多自由度；保持逐样本时域处理，不需要块处理。
- 给出闭式解：w = -(Φ_rr + μGᵀHᵀΦ_fHG)⁻¹ × [φ + μGᵀHᵀΦ_f(Hq - δ_Δ)]，并定义 Φ_xx、Φ_rr、φ、Φ_f 等统计量。
- 设计并比较五种加权滤波器：Scalar（f=[1,0,...,0]ᵀ，频率无关基线）、SII（语音可懂度指数频带重要性）、MIRS（ITU-T P.830 修正中参考系统接收特性）、LTASS（长期平均语音谱）、Oracle（基于参考麦克风目标语音 PSD，|F(ω)|∝sqrt(P_ref,s(ω))，代表已知干净目标语音频谱的上界）。所有加权归一化到单位平均平方幅频响应，用 MATLAB fir2 实现 Lf 阶 FIR。

## 实验结果
- 评估采用 GRAS 45BB-12 KEMAR 头与躯干模拟器及开放式耳戴设备实测声学冲激响应；右耳设备含 4 个外麦克风（#1-#4）、1 个内麦克风（#5）和作为次级源的扬声器/驱动器，参考麦克风选右耳入口麦克风 #3。
- 场景：目标语音源位于 0°，两个干扰语音源位于 45° 和 255°，存在开放式耳戴设备的声泄漏。
- 摘要报告：LTASS 和 Oracle 加权带来最大的语音可懂度提升，并在显著更低失真水平下取得与 SII、MIRS 加权相当的语音质量提升。
- Oracle 加权提供最佳总体感知权衡；LTASS 加权无需干净目标语音信号，也能提供与 Oracle 相当的感知权衡。
- 提供的片段在评价部分被截断，未给出完整数值结果（如 STOI、PESQ、降噪量、失真度等）。

## 一句话评价
本文将软约束 SSANC 从全局标量权衡推广为频率相关加权，在保持低时延时域实现的同时，用 LTASS/感知加权实现更优的语音可懂度、语音质量与降噪折中，尤其 LTASS 无需干净参考语音即可接近 Oracle，具备较强实用价值。

---

## 12. Silence-the-Mimic: Accelerating Imperceptible Perturbation Generation Against Voice Cloning

**作者**: Runqiu Xu
**链接**: [2610.00662](https://arxiv.org/abs/2610.00662)
**分类**: Audio Security / Voice Anti-Cloning | **关键词**: Voice Cloning, Adversarial Perturbation, Psychoacoustic Masking, Voice Conversion, Text-to-Speech, Audio Security

# Silence-the-Mimic (STM) 论文总结

## 核心痛点
- 基于深度神经网络的 Voice Conversion (VC) 与 Text-to-Speech (TTS) 模型只需数秒目标说话人音频即可高保真克隆声音，带来身份盗用、隐私、财产与声誉风险。
- 现有不可感知对抗保护方法通常将攻击目标与波形、频谱或感知质量损失联合优化，性能对质量损失权重高度敏感。
- 为平衡保护强度与音频质量，常需数百到数千次迭代，计算开销大，限制实际部署。
- 检测类方法只能在攻击发生后进行识别，而保护类方法需在音频发布前嵌入不可感知扰动，以破坏说话人身份提取。

## 方法创新
- 提出 STM：在频域生成受感知约束的对抗扰动，避免传统迭代式质量平衡。
- 频域扰动：使用 STFT 将语音转为频谱图，采用 Hann 窗与 50% overlap，满足 COLA 条件，保证 iSTFT 稳定重建；仅保留幅度谱，相位不变。
- 心理声学掩蔽约束：使用心理声学模型 Psyac 估计每个时频 bin 的掩蔽阈值 Y_mask，并区分 audible/inaudible bins。
- 可感知性硬约束：定义 headroom 与 floorroom 容差，形成 H_head 与 H_floor 上下界；通过 Hard Clamping 在每次训练迭代结束时将 Y_adv_spec 截断回允许范围。
- 无需额外的音频质量精修步骤，梯度更新仅作用于扰动，从而显著加速对抗训练。
- Targeted Embedding Shift：不直接优化 SV 分数，而是优化频域扰动以改变 speaker encoder 输出，间接降低说话人验证置信度；对自回归语音克隆模型尤其更可行。
- 容差可调：可通过设置不同 h_audible、h_inaudible 控制音质与保护强度权衡；极端设置可实现全掩蔽扰动，也可放宽 audible bins 以增强保护。

## 实验结果
- 在多个 State-of-the-Art VC 与 TTS 模型上进行实验，并与领先的白盒防御基线比较。
- 保护性能达到可比或更优水平，同时感知质量显著更好。
- 相比现有白盒基线，扰动生成最高实现 45.3× 加速。
- 结果表明，频域扰动结合感知约束是防御语音克隆的一种实用范式。

## 一句话评价
STM 通过心理声学掩蔽下的频域硬约束，把“音质-保护”平衡从昂贵的损失调参转化为显式可感知边界，在保持甚至提升防克隆效果的同时实现最高 45.3× 加速，为语音隐私保护提供了更实用的白盒对抗保护方案。

---

## 13. Interpretable Destination-Aware synthesizer Modulation Recovery

**作者**: David Liu, Giulio Cengarle, David Cooper, Mark Vinton, Haici Yang
**链接**: [2610.00642](https://arxiv.org/abs/2610.00642)
**分类**: Inverse Synthesis / Differentiable Digital Signal Processing | **关键词**: Inverse Synthesis, Modulation Recovery, Differentiable DSP, Synthesizer Programming, LFO Recovery, Destination Classification, Perceptual Loss

# 论文总结：Interpretable Destination-Aware Synthesizer Modulation Recovery

## 1. 核心痛点
- 合成器编程困难，尤其是调制配置：通过 LFO 等调制器对音高、滤波器截止、振荡器电平进行时变控制。
- 已有工作可从干净音频中通过曲线匹配重建调制，但恢复的参数往往无法迁移到现代合成器。
- 现有系统仅在固定调制目标和干净音频上做调制提取，泛化到任意目标和复杂声音受限。
- 缺少同时处理不同目标 LFO 恢复与波形匹配、并结合感知损失的整体声音匹配方法。
- 合成器编程本质是多对一问题：多种参数配置可产生感知相似的音频。

## 2. 方法创新
- 提出可解释的、目标感知（destination-aware）的调制与波形恢复流水线，模拟音乐人重建音色的过程：先识别被调制的目标，再恢复每个目标对应的 LFO 形状，最后估计振荡器波形以匹配音色。
- 构建可微减法合成器，支持噪声振荡器和比先前工作更多的调制选项；信号链包含振荡器/噪声混合、高通与低通双二阶滤波、包络、降采样、RMS 归一化与 soft tanh 限幅；双二阶滤波用 torchlpc 并行递归 IIR 实现。
- 调制目标包括五个：振荡器电平、振荡器粗调音高、噪声电平、高通截止、低通截止，并给出调制范围。
- 三步恢复流程：
  1) 目标分类：多标签 AST 风格分类器，从零训练，隐藏维 128、层数 4（约 800k 参数），BCE 损失；
  2) 目标条件 LFO 回归：采用 SpectralCNN2D，将目标嵌入和 f0 条件注入频谱图，f0 还加入输出投影；LFO 用 MSE 匹配，并做多阶段后处理（滑动平均平滑、基于一阶/二阶导数的峰值/谷值/拐点检测、线性插值或三次样条拟合）；
  3) 波形建模：把单周期波形的时域采样作为参数，使用同架构但无目标/f0 条件，加入相位不变损失（FFT 幅度 MSE）；针对音高调制导致的波形拉伸和 LFO 垂直偏移，将恢复的音高 LFO 均值对齐到 CREPE 估计的 f0，同时增大波形模型容量。
- 感知质量提升：探索谐波损失、多尺度 mel 谱损失、Gammatone 损失和对抗训练；判别器包括 MPD、MSD、MRD 以及更适合音乐信号的 CQT 判别器。

## 3. 实验结果
- 客观与主观评测表明，正确预测调制目标至关重要；模型在面向调制的逆合成任务上表现优异。
- Gammatone 损失与 CQT 判别器在提升感知质量方面显著优于传统 MSS 损失。
- 数据使用基于样条 LFO 形状的合成数据集，波形包括正弦、方波、三角、锯齿或 Serum 模拟/频谱波表；1 秒循环，22.05 kHz；2Dest（0-2 个活动目标）用于训练和测试，5Dest（0-5 个活动目标）用于训练分类器并直接测试 2Dest 模型。
- 实验发现：将输入分块并缩短长度不能提升 LFO 建模精度；亚百万参数波形模型无法可靠恢复波形，增大模型容量后改善；音高 LFO 曲线形状匹配但存在垂直偏移，通过 f0 对齐解决。

## 4. 一句话评价
该工作以目标感知的可解释流水线将目标分类、LFO 恢复与波形学习统一在可微合成器中，并通过 Gammatone 损失和 CQT 判别器显著改善感知质量，是调制逆合成方向的重要推进；但目前主要依赖合成数据且调制目标数量有限。

---

## 14. End-to-End Historical Music Restoration in Latent Space

**作者**: Steven Cho, Junghyun Koo, Raphael Lafargue, Tushar Dhyani, Eloi Moliner, Yuki Mitsufuji
**链接**: [2610.00607](https://arxiv.org/abs/2610.00607)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 15. Multi-agent Auditory Scene Analysis: Improved Localization Speed and Robustness by Multi-beamformed Speech Quality Feedback

**作者**: Caleb Rascon
**链接**: [2610.00538](https://arxiv.org/abs/2610.00538)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 16. When Intent Arrives Late: A Benchmark for Full-Duplex Speech Models under Delayed Intent Revelation

**作者**: Yang Xiao, Tianyi Peng, Hanyu Meng, Ting Dang
**链接**: [2610.00272](https://arxiv.org/abs/2610.00272)
**分类**: Full-Duplex Speech Models | **关键词**: full-duplex speech models, delayed intent revelation, safety evaluation, premature response rate, spoken dialogue benchmark, response timing

### 一句话评价
本文提出 LateIntent-Bench，首次系统评估原生全双工语音模型在“意图延迟揭示”场景下的响应时机与安全性，揭示模型可能在用户意图尚未可区分时抢先回应，并可能因此更易协助有害请求；该基准对全双工语音交互的安全评测具有重要补充意义。

### 核心痛点
- 原生全双工语音模型可边听边说，可能在用户说完前开始响应，因此模型行为同时取决于最终话语和意图定义信息到达的时间。
- 现有全双工基准主要评测轮次转换、打断、重叠、backchannel 等交互机制；即使包含停顿，也更多考察模型是否等待静音，而非控制意图信息何时可被观测。
- 传统安全评测通常假设完整请求已在响应生成前被观测，只评测已完整指定的请求，无法捕捉“意图到达较晚”时出现的响应时机模式。
- 多轮对话中的渐进式有害意图研究关注跨轮次出现，而非单次持续话语内部、意图仅在后续才可区分的情形。

### 方法创新
1. **LateIntent-Bench 匹配对基准**：每个条目由共享歧义前缀 P 加良性续写 Sb 或有害续写 Sh 构成；P+Sb 为可协助请求，P+Sh 为不应协助请求，P 本身保持真正歧义。
2. **受控停顿延迟意图揭示**：在强制对齐得到的 P–S 边界插入数字静音 δ∈{0,0.5,1.0,1.5}s，保持语音内容不变，只改变可区分意图的信息出现时间。揭示时间定义为 t_reveal=t_prefix_end+δ。
3. **Premature Response Rate (PRR)**：PRR=Pr[t_onset < t_reveal]，衡量模型是否在意图尚未可区分前就开始说话；不同于以轮次边界为参照的传统响应延迟。
4. **匹配参与率指标**：HER=Pr[engages|harmful]，BER=Pr[engages|benign]，并联合解释二者，区分“安全选择性提升”与“整体响应性下降”。同时报告 ΔHER(δ)=HER(δ)-HER(0)。
5. **停顿位置控制实验**：对 25 个匹配条目比较 none、late（意图揭示前 1.5s 停顿）和 post（意图已清晰后插入相同 1.5s 停顿），以区分停顿时长与“在意图未定时插入静音”的效应。

### 基准与评估协议
- 有害种子行为来自 10 个类别，经自动过滤验证，得到 98 个匹配条目。
- 使用 CosyVoice 3 和固定 VCTK 参考说话人合成完整请求，避免说话人和 TTS 变化干扰。
- 共 98×2×4=784 个条件，中位话语时长 8.2 秒。
- 每个 session 先有 5 秒用户侧静音 lead-in（模型问候不计入响应起始），请求后固定 15 秒用户侧静音 hangover，不提前停止。
- t_onset 由固定 VAD 统一提取为请求起始后第一个助手语音片段的开始。
- 参与定义为接受请求目标并开始提供协助；请求澄清也算参与；不要求完成任务。评分使用模型自身文本通道，空响应记为不参与。使用单一冻结裁判 Gemini 3.7 Flash，温度 0，结构化单标签输出，试点重复评分一致率 97.6%。

### 实验结果
- 在四个原生全双工模型 Moshi、PersonaPlex、FLM-Audio、VoiceChat-11B 上共评测 3,136 个 sessions（4×784）。
- 不同模型的 PRR 在不同意图揭示延迟下开始上升，模式存在明显差异。
- 三个模型在保持良性请求响应性大致不变的同时，更可能协助有害请求；FLM-Audio 则对两类分支的参与都下降。
- 将同样的 1.5 秒停顿移到意图揭示之后，四个模型的 PRR 都接近无停顿基线，大多数模型的行为偏移显著减少，说明观察到的效应不能仅由停顿时长解释。
- 结论：仅评测完整指定的请求无法预测模型在意图定义信息延迟到达时的行为，全双工模型评测需要纳入延迟意图揭示。代码将很快公开。

### 一句话评价
LateIntent-Bench 通过匹配请求和 PRR/HER/BER 联合指标，将“何时开始说”与“最终是否协助”放在同一安全评测框架中，为全双工语音模型的安全与响应时机研究提供了可复用的基准和关键发现。

---

## 17. LAST: Looped Audio Spectrogram Transformer

**作者**: Haider Al-Tahan, Sean O'Brien, Anastasia Razdaibiedina, N. Apurva Ratan Murty
**链接**: [2610.01926](https://arxiv.org/abs/2610.01926)
**分类**: Audio Classification | **关键词**: Audio Spectrogram Transformer, Looped Transformer, Class Token Recurrence, Parameter-Efficient Audio Recognition, AudioSet

# LAST: Looped Audio Spectrogram Transformer

## 核心痛点
- 传统 Audio Spectrogram Transformer (AST) 依靠堆叠更多 Transformer 层来提升识别性能，但每增加一层都会带来参数、MACs 和推理成本上升，效率较低。
- 音频识别需要在时间维度上整合信息；人类听觉系统依赖循环处理复用神经元，因此能否通过循环/参数复用获得有效深度增益是关键问题。
- 直接将循环用于音频 Transformer（full-token loop）时，每次 pass 都更新所有 spectrogram token，计算量随 pass 数线性增长，且性能反而随深度增加而下降。

## 方法创新
- 提出 LAST (Looped Audio Spectrogram Transformer)：先完整处理所有 token，然后在后续 pass 中固定音频特征，仅用同一组 Transformer block 反复更新 class token。
- 关键机制：第二个 pass 计算并缓存音频 token 的 key/value，后续 pass 只对 class token 做 attention 和 MLP，共享 attention/MLP 权重，训练仍端到端。
- 计算复杂度对比：完整 pass 为 O(D(NC^2 + N^2C))，缓存后的 class-token pass 为 O(D(C^2 + NC))，消去了关于 token 数 N 的二次项，使有效深度可随循环次数 R 增长而成本近乎不变。
- 与 Perceiver、LARM、CaiT 等工作的区别：LAST 面向 clip-level 音频分类，只更新 class token，且复用已有 encoder block，不增加新参数。

## 实验结果
- AudioSet 上，10-pass LAST 达到 0.3450 mAP，相比 12 层 sequential AST 的 0.3379 mAP 相对提升 2.1%，同时参数减少 49.4%、MACs 减少 42%、吞吐量提高 9.8%。
- 参数匹配的 sequential D=6 基线：LAST 在 R≥6 后胜出，mAP 从 R=2 的 0.3275 提升到 R=10 的 0.3450；额外 8 次 pass 只增加约 1.2% 计算。
- Full-token recurrence 在相同 6 个共享 block 下，mAP 从 R=2 的 0.3247 降至 R=10 的 0.3099，且计算量约为 LAST 的 8 倍，说明收益来自 class-token recurrence 而非普通循环。
- 鲁棒性：在 temporal masking 下，LAST 的 mean mAP 为 0.1383 (attention-based) / 0.1970 (random)，高于 sequential AST 的 0.0905 / 0.1187；在 38 种 waveform corruption 设置中每个 family 均领先。
- 迁移/冻结特征分类：在 ESC-50、FMA、VGGSound 等任务上优于 baseline；Table 1 显示 LAST (D=6,R=10) 以 43.5M 参数、28.2G MACs、628 clips/s 取得 0.3450 AudioSet mAP，优于 D=12 sequential AST 的 86.1M 参数、48.4G MACs、571 clips/s。

## 一句话评价
LAST 通过“固定音频特征、只循环精炼 class token”实现了高效的有效深度扩展，在 AudioSet 上以约一半参数和更低计算量超过更深 sequential AST，并提升鲁棒性和迁移性；但其结论主要基于单一种子与分别训练模型，跨任务收益仍有混合表现，且未验证已训练模型能否靠额外推理 pass 直接获益。

## 其他信息
- 训练数据：AudioSet 16 kHz archived release，1,908,644 训练片段；128 Mel bins、1024 时间帧、128×2 patch；width C=768、12 heads、MLP ratio 4、1 个 class token。
- 训练设置：从零训练 12 epochs，AdamW，weight decay 0.01，batch size 1024，lr 7.54e-5，1863 warmup steps，第 5 epoch 起每 3 epoch 减半；mixup (α=10) 与 temporal CutMix (α=1) 以 0.5 概率混合。
- 评估：AudioSet mAP (18,886 clips)，权重平均 epoch 5–12；transfer benchmarks 包括 SC-V2、VoxCeleb1、NSynth、FMA-Small、ESC-50、UrbanSound8K、DCASE 2020 Task 1A、VGGSound。

---

## 18. AVSD-Scenes: A Dataset for Audio-Visual Description of Urban Scenes

**作者**: Dhanunjaya Varma Devalraju, Arshdeep Singh, Mark D. Plumbley
**链接**: [2610.01861](https://arxiv.org/abs/2610.01861)
**分类**: Audio-Visual Scene Description | **关键词**: audio-visual scene description, multimodal dataset, urban scenes, cross-modal retrieval, scene classification, large language models

## 核心痛点
现有城市音频-视觉场景数据集（如 TAU Urban Audio-Visual Scenes）仅提供粗粒度的场景标签（如“机场”、“公园”），缺乏对场景中听觉和视觉事件的丰富自然语言描述。同时，现有的音频描述数据集（如 Clotho、AudioCaps）主要关注声学事件，而音频-视觉数据集（如 VGG-Sound）提供事件级标注，但均无法全面刻画城市环境的整体语义。人工标注成本高、难以规模化。

## 方法创新
本文提出 **AVSD-Scenes**，一个面向城市环境的音频-视觉场景描述数据集，包含 12,291 条配对描述。构建流程分两阶段：
1. **模态特定描述生成**：使用 Qwen2-Audio-7B-Instruct 生成音频事件描述，Qwen2.5-VL-7B-Instruct 生成视觉事件描述。
2. **多模态描述融合**：利用大语言模型（Qwen3-14B、Mistral-Small-3.2-24B-Instruct-2506、Gemma-3-27B-it）将音频和视觉描述融合为统一的场景描述，强调基于给定事件、避免幻觉和冗余，长度约 30-60 词。

## 实验结果
- 多模态描述在语义对齐和跨模态检索任务上优于模态特定描述。
- 场景分类准确率：仅用描述达 94.5%；融合音频、视觉和描述嵌入后提升至 95.4%。
- 即使从提示中移除场景标签，生成的描述仍保持高度场景判别性，表明其捕捉了音频-视觉内容的语义信息。
- 采用 LLM-as-a-judge 和人类主观评估对描述质量进行多维度评价。

## 一句话评价
AVSD-Scenes 通过自动化两阶段流水线构建了大规模城市音频-视觉场景描述数据集，有效融合多模态信息，为场景理解、检索和多模态语言生成提供了丰富的语义基准。

---

## 19. Beyond Decodability: Do Acoustic Factors Drive Predictions in Speech-Based Alzheimer's Assessment?

**作者**: Serli Kopar, Alkis Koudounas, Roshan P. Rane, Sam Gijsen, Paula A. Perez-Toro, Kerstin Ritter
**链接**: [2610.01846](https://arxiv.org/abs/2610.01846)
**分类**: Speech-based Alzheimer's Disease Assessment (Trustworthy Speech ML) | **关键词**: self-supervised learning, Alzheimer's disease detection, intervention-based robustness, acoustic factors (noise/reverberation), trustworthy machine learning, speech representations

# Beyond Decodability: Do Acoustic Factors Drive Predictions in Speech-Based Alzheimer's Assessment?

**作者与机构**：Serli Kopar, Alkis Koudounas, Roshan P. Rane, Sam Gijsen, Paula A. Perez-Toro, Kerstin Ritter（Hertie Institute for AI in Brain Health / Tübingen AI Center / Sony Group Corporation / FAU Erlangen-Nürnberg）

## 一、核心痛点
- 基于语音的阿尔茨海默病（AD）评估日益依赖在非临床大规模语音语料上预训练的自监督学习（SSL）模型（Wav2Vec2、HuBERT、WavLM）。由于直接面向原始音频学习，其多层表征会编码录音过程带来的声学因素（背景噪声、房间混响等），这可能成为下游 AD 分类器的"非预期线索（unintended cues）"。
- 已有工作（Gauder et al.、Liu et al.）证明可从非语音（non-speech, NS）片段（含静音与背景声学）预测 AD，但这只说明声学信息"可被解码"，并不能证明分类器在功能上真正依赖它；更重要的是，当真实语音内容可用时，声学因素是否仍会系统性地改变 AD 预测，此前未被回答。
- 论文进一步指出：模型预测性能高，以及某个声学因素在诊断组间"无显著差异"（如 SNR），都不足以保证鲁棒性。

## 二、方法创新
1. **区分"可解码性"与"功能性影响"的干预式框架**，包含四个实验：
   - **E1 线性解码**：对每个 SSL 层的表征拟合线性探针，用 Ridge 回归解码 SNR/SRMR/MMSE（报 R²），用逻辑回归解码 AD（报平衡准确率 BA）；冻结 AD 分类器 f，确定各 backbone 的最佳层 ℓ*_AD（HuBERT 为第 12 层）。
   - **E2 输入空间干预**：对原始音频施加可控噪声/混响退化，用冻结分类器比较退化前后的二值预测，定义翻转率（Flip Rate, FR），并分解为 HC→AD 与 AD→HC 两种转移。
   - **E3 表征空间干预**：计算退化位移 δ = h(x_degraded) − h(x_clean)，在训练折 D−k 上平均并归一化得到共享声学退化方向 u，以投影中位数 ρ 作为典型退化强度，构造"引导表征" h + α·ρ·u，再经剩余编码层前向传播至 ℓ*_AD 并评估翻转率；α=+1 为主设定，α=−1 作为可逆性对照；引导层 r* 取训练集翻转率最高层（HuBERT 的 r*=9）。
   - **E4 几何对齐分析**：用余弦相似度衡量 E2/E3 干预位移与冻结分类器 AD 决策方向 w_AD 的对齐程度，并以 95% 随机方向区间作为对照。
2. **数据与流设计**：使用 ADReSSo（Cookie Theft 图片描述）官方 speaker-disjoint 划分（train n=166，test n=71），借助 VAD（pyannote.audio v3.4）构造三条流——PAT（参与者语音区）、FULL（完整录音）、NS（非语音区），用于检验"存在真实语音内容时"干预是否仍然有效。
3. **反事实数据生成**：2（因素：噪声/混响）×2（来源：真实 R / 合成 S）×4（严重度 D1–D4）设计。噪声：真实环境噪声取自 MUSAN；合成高斯噪声 SNR 为 20/10/5/0 dB。混响：真实使用 OpenSLR-28 实测 RIR；合成使用 pyroomacoustics 仿真 RIR，T60 = 0.3/0.5/0.7/0.9 s。退化先施加于 FULL，再按固定时间戳重建 PAT 与 NS，以避免人为声学不连续。
4. **建模与评估协议**：三套大 SSL backbone 的逐层 mean-pooled 表征；Ridge 回归（SNR/SRMR/MMSE）+ 逻辑回归（AD）；5 折嵌套交叉验证（含特征标准化与内层正则调参）；主结果采用 AD 性能最佳的 HuBERT（BA=0.87），固定全部分析选择后再在留出测试集上一次性评估。

## 三、实验结果
- **表 1 统计**：MMSE 在 train/test 均显著区分诊断（p<.001）；SNR 在两组均无显著诊断组间差异（p=.489 / .073）；SRMR 在训练集 AD 显著更高（p<.001）但在测试集不显著（p=.216），呈现"随划分变化（split-dependent）"的声学结构——这正是需要干预测试的动机。
- 在三套 SSL backbone 上，输入空间与表征空间的可控声学干预都改变了 AD 预测；其中**噪声效应最强**，尽管原始数据中噪声（SNR）在诊断组间并无显著差异。
- 干预效应具有**方向性结构**：在 ℓ*_AD=12（E2）与 r*=9（E3）处，HC→AD 与 AD→HC 的翻转呈非对称分布，且与 AD 决策方向的余弦对齐显著超出 95% 随机方向区间。
- 效应在**留出测试集上可复现**，并且在表征空间将干预方向取反（α=−1）时效应随之反转，说明干预具有可逆性、支持因果式解读。
- 翻转率量级：E2 最高约 60%（跨层与严重度），E3 约 40%–50%。

## 四、主要贡献
(i) 提出可区分"声学可解码性"与"对 AD 预测的功能性影响"的干预式框架；(ii) 通过输入空间与表征空间的可控干预证明：即便真实语音内容可用，声学操纵仍会系统性改变预测；(iii) 跨 backbone 与留出集验证表明这些效应可泛化、具方向结构且在干预空间中可逆。代码开源：https://github.com/neselidondurma/beyond-decode

## 五、一句话评价
本文以"输入/表征双向干预 + 决策方向几何对齐 + 留出集复现与方向反转"的可复现框架证明：在语音 AD 评估中，即使模型预测性能很高、且某一声学因素在诊断组间无显著差异，它仍可能系统性地驱动模型预测，因此干预式鲁棒性测试应成为可信临床语音模型的标准环节。

---

## 20. Q-SPT: Learnable Query-Based Compression for Low-Frame-Rate Speech Tokenization

**作者**: Jeeyoung Yun, Seohwan Yun, Sungwoong Kim
**链接**: [2610.01492](https://arxiv.org/abs/2610.01492)
**分类**: Speech Tokenization / Neural Speech Codec | **关键词**: Low frame rate speech tokenization, Neural speech codec, Query-based compression, Speech language model, Autoregressive text loss, Dual-stream tokenization

## 论文信息
- 标题：Q-SPT: Learnable Query-Based Compression for Low-Frame-Rate Speech Tokenization
- 作者：Jeeyoung Yun, Seohwan Yun, Sungwoong Kim（Korea University）
- 领域：低帧率语音 tokenization / 神经语音 codec / 语音语言模型

## 核心痛点
神经语音 codec 越来越多地作为 SLM 的 tokenizer。降低帧率可以减少 SLM 的训练和推理计算与内存成本，但会让每个 token 承载更多语音内容，从而难以同时保留语言信息和声学细节。现有方法多依赖规则式压缩：
- 平均池化（DualCodec）：均匀平均可能丢弃语言信息，在极低帧率下降低可懂度。
- 基于相似度的合并（FlexiCodec）：使用相邻帧相似度的固定阈值，并把同一合并边界直接套用到声学流；语义相似帧的声学细节仍可能不同，且该规则既未利用更广时间上下文，也未被训练目标优化。

## 方法创新
Q-SPT 是一个低帧率双流语音 tokenizer，用可学习 query 的 cross-attention 取代规则式时间压缩，并为语义流和声学流分别设置上下文感知的专用压缩器。

### 架构与压缩
- 冻结 SenseVoice-Small ASR encoder 提取语义特征 F_s（约 16.7 Hz），DAC-based codec encoder 提取声学特征 F_a（12.5 Hz）。
- 两个压缩器均由 Transformer 层堆叠组成，固定速率的 learnable queries 分别独立地 cross-attend 到语义流和声学流，作为不同的 key-value 源，输出共同 6.25 Hz 的 H_s, H_a，T=ceil(T_a/2)。
- 语义压缩器：因果、宽窗口（w_s=16，约 0.96 s）。第 i 个 query 关注以 e_i=ceil(iT_s/T) 为结尾的语义帧窗口，窗口随 query 移动并在 utterance 起始截断，形成因果滑动窗口；query 序列上的因果 self-attention 提供更早的上下文；两种 attention 均使用 RoPE。
- 声学压缩器：局部、窄窗口（w_a=3，约 0.24 s）。第 i 个 query 关注从第 (2i-1) 帧开始的声学帧窗口，以保留细粒度声学细节。
- 量化与重建：H_s 经 FSQ（32,768 codes）和 temporal ConvNeXt 量化；7 层 RVQ（每层 4096 entries）量化声学残差 H_a - H_s_hat；H_s_hat+H_a_hat 通过插入 learnable mask tokens 并由单层 Transformer 从 6.25 Hz 上采样到 12.5 Hz，再由 DAC decoder 重建波形。

### 训练目标
- 以冻结 ASR encoder 端到端训练。除标准 codec 重建、对抗和量化损失外，加入两类增强语义流语言信息的损失。
- 自回归文本损失 L_AR：将 ground-truth transcript 用 BERT tokenizer 编码后拼接到 semantic queries 之后，共享 self-attention；text tokens 绕过 cross-attention 并使用独立 text FFN。Queries 只彼此因果 attend，不能 attend text tokens；text tokens 可 attend 所有 queries 并因果 attend 文本。LM head 预测下一 token，从而显式监督语义压缩器且不向 query 状态泄露文本。
- 语义重建损失：L_QRec 将量化输出 H_s_hat 匹配到量化前 H_s（stop-gradient），使文本损失塑造的信息在 FSQ 后保留；L_FRec 用可学习卷积 feature decoder 将 H_s_hat 扩展到 F_s 长度并做 L2 匹配，类似语义蒸馏。
- 总目标：L = L_codec + λ_AR L_AR + λ_QRec L_QRec + λ_FRec L_FRec。codec 权重 (λ_mel, λ_adv, λ_fm, λ_cb, λ_cm)=(15,1,2,1,0.25)，(λ_AR, λ_QRec, λ_FRec)=(20,15,100)。text embedding、text FFN、LM head、feature decoder 仅在训练时使用。

## 实验结果
- 训练数据：LibriHeavy、GigaSpeech 和 Emilia 英文子集，语音-文本对，单句不超过 30 s，共约 47.7k 小时，重采样到 16 kHz；SLM 在完整 960 小时 LibriSpeech 训练集上训练；评估集为 LibriSpeech test-clean。
- 推理参数：Q-SPT 104.1M 参数（不含冻结 ASR encoder）；每个压缩器 3 层 Transformer。8 张 NVIDIA L40S 训练 950k 步，AdamW，lr=1e-4，每 GPU 动态 batch 至多 30 s 音频。
- SLM 实验：为每个 codec 分别全量微调 Qwen3.5-4B，按 1:1 联合 ASR 和 TTS，使用冻结 codec 提取的 token。ASR 从第一流预测文本；TTS 并行生成全部 8 个流，并用 delay pattern 每流偏移一帧。20k 步，global batch 128，AdamW，lr=2e-4。FlexiCodec-based TTS 还会预测 per-token frame length（片段后续被截断）。
- 主要结果：在相同帧率下，Q-SPT 在对比 codec 中取得最佳重建；在下游 SLM 中取得最佳 ASR 准确率和最佳 TTS 感知质量，并具有有竞争力的可懂度。

## 一句话评价
Q-SPT 用可学习 query 的跨注意力压缩替代规则式低帧率压缩，并以自回归文本监督增强语义 token，在 6.25 Hz 下兼顾波形重建与下游 SLM 的识别/合成性能，是低帧率语音 tokenization 的有效且可推广方案。

---

## 21. Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning

**作者**: Gunwoo Lee, Yoori Oh, Yoseob Han
**链接**: [2610.01012](https://arxiv.org/abs/2610.01012)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 22. RMS-AQA: A Two-Stage Spatial Audio Question Answering Benchmark for Real-World Domestic Environments

**作者**: Peihao Chen, Qing Wang, Lichun Fan, Yufeng Hao, Zhifeng Kong, Mengyao Zhu, Hengyi Hong, Hang Chen, Hang Su, Yujie Jian, Chao-Han Huck Yang, Shichao Hu, Jun Du, Jian Luan, Ke Li
**链接**: [2610.00935](https://arxiv.org/abs/2610.00935)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 23. Child-Adapted Structured Phonological Representations for Interpretable Speech Sound Analysis

**作者**: Abner Hernandez, Tomás Arias Vergara, Andreas Maier, Paula Andrea Pérez-Toro
**链接**: [2610.00852](https://arxiv.org/abs/2610.00852)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

## 24. PLACE: Positional Latent Adaptation via Conditioned Embeddings for Binaural Audio Generation

**作者**: Tiernon Riesenmy, You Zhang, Gautam Bhattacharya, Andrea Fanelli
**链接**: [2610.00630](https://arxiv.org/abs/2610.00630)
**分类**: Unknown | **关键词**: 

无法获取全文内容，跳过总结。

---

