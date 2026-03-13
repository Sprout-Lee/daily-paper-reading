# Arxiv Daily Deep Report - 2026-03-13

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 16
---

## 1. Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition

**作者**: Umberto Cappellazzo, Stavros Petridis, Maja Pantic
**链接**: [2603.12046](https://arxiv.org/abs/2603.12046)
**分类**: Audio-Visual Speech Recognition | **关键词**: Audio-Visual Speech Recognition, Shapley Values, Modality Contribution

# 核心痛点
音频-视觉语音识别（AVSR）模型在利用音频和视觉信息时，模态贡献平衡不明确，尤其是在干净条件下，模型倾向于音频偏向，视觉贡献不明显，导致对噪声的鲁棒性有限。

# 方法创新
提出 Dr. SHAP-AV 框架，使用 Shapley 值量化模态贡献，引入三种分析：Global SHAP 用于整体模态平衡，Generative SHAP 用于解码过程中的贡献动态，Temporal Alignment SHAP 用于输入-输出对应关系。该方法扩展了 Shapley 值到跨注意力架构，并支持多粒度分析，超越静态归因。

# 实验结果
在六个 AVSR 模型（AV-HuBERT、Auto-AVSR、Whisper-Flamingo、Llama-AVSR、Llama-SMoP、Omni-AVSR）和 LRS2、LRS3 基准测试上实验，发现：1) 随着音频质量下降，模型向视觉依赖转移，但即使在 -10 dB SNR 下，音频贡献仍保持 38-46%；2) 模态平衡在生成过程中演化，不同模型表现各异；3) 模态时间对齐在噪声下保持稳健；4) 不同噪声类型诱导不同程度的视觉依赖；5) 话语长度影响模态贡献，模型特定；6) SNR 是模态平衡的主导因素，识别难度影响最小。

# 一句话评价
这项研究通过 Shapley 值为 AVSR 提供了深入的模态行为洞察，揭示了持久音频偏向，推动了显式模态加权机制的发展，并鼓励将 Shapley 值作为标准诊断工具。

---

## 2. Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review

**作者**: Kele Xu, Yifan Wang, Ming Feng, Qisheng Xu, Wuyang Chen, Yutao Dou, Cheng Yang, Huaimin Wang
**链接**: [2603.11877](https://arxiv.org/abs/2603.11877)
**分类**: Speech Recognition | **关键词**: Silent Speech Interface, Large Language Models, Articulatory sensing

# 核心痛点
- 传统人机交互依赖声学通道，自动语音识别系统易受环境噪声（如非平稳噪声和高混响）影响，导致性能下降。
- 声学依赖导致隐私泄露风险，在公共或共享空间中引发社交摩擦。
- 对语音障碍人群（如喉切除或神经退行性疾病患者）的包容性差，排除其使用。

# 方法创新
- Silent Speech Interfaces (SSIs) 通过直接从神经-肌肉-发音链解码语言意图，绕过声学通道。使用多种传感模态：神经振荡（如EEG/ECoG）、神经肌肉激活（如sEMG）、发音运动学（如超声波/磁测法）和主动探测（如声学或射频传感）。
- 整合大型语言模型和深度生成架构作为高级语言先验，通过潜语义对齐解决生物信号的“信息稀疏性”和非平稳性问题，将碎片化生理特征映射到结构化语义潜在空间。
- 技术从传统启发式信号处理过渡到基于Transformer和扩散的架构，并利用自监督基础模型减少用户依赖性。

# 实验结果
- SSI框架通过映射到语义潜在空间，首次接近了现实世界部署所需的Word Error Rate可用性阈值。
- 技术已从笨重实验室仪器过渡到集成于商品级可穿戴设备的“隐形接口”，如耳戴设备和智能眼镜，实现更高鲁棒性和实用性。
- 在开放词汇连续语音任务中，通过多模态对比学习和LLM条件重评分，达到前所未有的准确性。

# 一句话评价
- 这篇论文提供了SSI领域的全面分类和系统综述，强调了LLM时代的技术革新，并提出解决挑战和伦理问题的战略路线图，推动该领域向实际应用发展。

---

## 3. Reconstruction of the Vocal Tract from Speech via Phonetic Representations Using MRI Data

**作者**: Sofiane Azzouz, Pierre-André Vuissoz, Yves Laprie
**链接**: [2603.11847](https://arxiv.org/abs/2603.11847)
**分类**: Acoustic-to-Articulatory Speech Processing | **关键词**: Acoustic-to-articulatory, Speech production, Vocal tract shape, MRI data, Phonetic segmentation

## 核心痛点
传统声学-发音倒置方法依赖有限数据，如电磁发音仪（EMA）存在传感器数量少、干扰发音等局限性；实时动态MRI（rt-MRI）数据质量低、分辨率差、数据集小，且缺乏可靠轮廓跟踪工具，阻碍了准确发音道重建。
## 方法创新
本研究采用高分辨率（136×136像素）rt-MRI数据，通过自动轮廓跟踪提取发音轮廓而非全图像；创新性地比较三种语音分割级别：基于Wav2Vec 2.0的自动转录、使用Astali的强制对齐分割、专家手动校正分割，并与MFCCs基线对比，评估语音信息纳入的效果。模型架构基于Bi-LSTM，输入改为语音表示而非原始语音信号。
## 实验结果
基线模型（使用MFCCs）表现最佳，平均RMSE为1.51 mm；语音分割方法中，专家校正模型RMSE为1.61 mm，接近基线但略差，其他方法（Wav2Vec 2.0和Astali）性能更差。结果表明，直接使用MFCCs可能更有效，手动校正的额外预处理努力收益有限。
## 一句话评价
该研究评估了语音信息在发音道重建中的作用，发现基于MFCCs的简单方法优于复杂语音分割，为权衡预处理成本与精度提供了实用见解。

---

## 4. Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model

**作者**: Sofiane Azzouz, Pierre-André Vuissoz, Yves Laprie
**链接**: [2603.11845](https://arxiv.org/abs/2603.11845)
**分类**: Acoustic-to-Articulatory Inversion | **关键词**: Acoustic-to-Articulatory Inversion, Clean Speech, rt-MRI, HuBERT, Bi-LSTM

**核心痛点**: MRI环境下的语音录音受扫描仪噪声污染，即使去噪后也与清洁语音有显著差异（如能量降低和高频损失），限制了声学-发音反转在实际应用中的可行性，因为真实场景通常需要清洁语音输入。

**方法创新**: 提出使用清洁语音作为去噪MRI语音的替代方案，以提升实用性。开发了基于语音分割的分层对齐算法，从句子到音素逐级对齐MRI和清洁语料库，确保时间一致性。采用自监督学习模型HuBERT-Base作为输入特征提取器，结合神经网络架构（两个全连接层和两个Bi-LSTM层），输出八个发音器官的轮廓坐标（共50个点），使用均方误差损失函数进行回归优化。

**实验结果**: 通过三种实验配置评估：M2M（MRI语音训练和测试）、M2C（去噪MRI语音训练、清洁语音测试）、C2C（清洁语音训练和测试）。C2C配置达到均方根误差1.56毫米，接近M2M的1.51毫米，表明清洁语音能有效支持发音反转，性能与基于MRI的方法相当；M2C配置性能下降，显示训练数据与测试数据不匹配的影响。实验还验证了对齐方法的重要性，使用动态时间规整（DTW）对齐后性能略有下降。

**一句话评价**: 这项研究证明了清洁语音在声学-发音反转中的有效性，性能接近基于MRI的方法，为医疗、语音技术等实际应用提供了更便捷、低噪声的解决方案。

---

## 5. ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping

**作者**: Ivan Yakovlev, Anton Okhotnikov
**链接**: [2603.11841](https://arxiv.org/abs/2603.11841)
**分类**: Speaker Verification | **关键词**: speaker verification, time-pooling, neural network architecture

# 核心痛点
原始 ReDimNet 架构中，为了保持时间分辨率（T）不变，通道维度（C）的扩展导致 1D 处理路径的计算成本呈二次增长，限制了模型的可扩展性和效率，在说话人验证任务中难以平衡计算资源与准确性。

# 方法创新
ReDimNet2 通过引入时间维度池化（time-pooling）在 1D 处理路径中，减少时间步数，从而在保持残差连接和维度重塑逻辑有效的同时，允许更激进的通道扩展。具体改进包括：在中间阶段应用时间池化（如 halving T），使用上采样对齐不同时间分辨率的特征图以维持残差连接，并释放计算预算用于增加通道数，实现双重效率提升（1D 和 2D 路径均受益）。

# 实验结果
在 VoxCeleb1 基准测试中，ReDimNet2 提供了七种配置（B0-B6，参数范围 1.1M 到 12.3M，计算成本 0.33 到 13 GMACs）。与原始 ReDimNet 相比，在所有规模点上均改善了计算成本（GMACs）与准确性（EER）的帕累托前沿。例如，B6 配置在 Vox1-O 上达到 0.287% EER，比 ReDimNet-B6 提高 28% 相对准确性，同时减少 36% 计算成本和 18% 参数。此外，ReDimNet2 在更大规模模型中表现更佳，并在域外测试集上展示了更好的泛化能力。

# 一句话评价
ReDimNet2 通过简单而创新的时间池化策略，有效解决了说话人验证模型的可扩展性问题，在保持高准确性的同时显著提升了计算效率。

---

## 6. Affect Decoding in Phonated and Silent Speech Production from Surface EMG

**作者**: Simon Pistrosch, Kleanthis Avramidis, Tiantian Feng, Jihwan Lee, Monica Gonzalez-Machorro, Shrikanth Narayanan, Björn W. Schuller
**链接**: [2603.11715](https://arxiv.org/abs/2603.11715)
**分类**: Speech Emotion Recognition | **关键词**: affect decoding, surface EMG, silent speech, emotion recognition, paralinguistics

### 核心痛点
传统语音情感研究主要依赖声学分析，但底层发音运动执行与情感的联系尚不清楚，尤其是在声学信息有限或不可用的环境中（如无声语音界面和辅助通信技术），情感解码面临挑战。
### 方法创新
本研究创新性地使用表面肌电图（sEMG）记录面部和颈部肌肉活动，系统比较发声和无声语音产生中的情感解码；引入一个包含2,780个话语、12名参与者的多任务数据集，评估个体内和个体间解码性能；结合多种特征和模型嵌入进行分析，并设计消融实验探讨情感签名的持久性。
### 实验结果
EMG表示能可靠解码挫折情感，最高AUC达0.845；情感签名在无声语音中持续存在，表明其嵌入在运动活动中；解码性能在个体间和不同发音模式中泛化良好，突出了sEMG在情感感知应用中的潜力。
### 一句话评价
这项研究为EMG-based情感解码提供了实证基础，特别推动了无声语音界面向更自然、表达性通信的发展。

---

## 7. RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

**作者**: Yongjoon Lee, Jung-Woo Choi
**链接**: [2603.11678](https://arxiv.org/abs/2603.11678)
**分类**: Speech Synthesis | **关键词**: Relativistic Adversarial Feedback, GAN Vocoders, Self-Supervised Learning, Perceptual Quality

# 论文总结：RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

## 核心痛点
GAN-based vocoders 在语音合成中面临效率和泛化能力的权衡问题。现有方法如扩散模型（Diffusion-based frameworks）和 Flow Matching（FM）虽然提高了泛化能力，但往往牺牲了计算效率；而传统 GAN vocoders 如 BigVGAN 在泛化时效率下降。这导致需要一种方法在保持 GAN 高效性的同时，增强对未见数据（如新说话人或风格）的泛化性能。

## 方法创新
提出 Relativistic Adversarial Feedback（RAF），一种新颖的 GAN 训练框架。RAF 包括两个核心组件：
1. **质量差距**：利用自监督学习（SSL）模型（如 WavLM 和 HuBERT）和 Multi-resolution STFT（M-STFT）距离来量化生成波形与真实波形之间的感知差异，从而提供更丰富的质量评估。
2. **判别器差距**：采用相对性配对 GAN（RpGAN）的思想，通过相对性反馈鼓励判别器为每个真实/伪造样本对分配独立决策边界，而非全局边界。这促进了对训练数据分布的更全面覆盖。
RAF 的训练目标是最小化 SSL 辅助的判别器差距，通过对抗反馈提升生成器的表示学习能力。

## 实验结果
- 在多个数据集（包括一个源数据集和四个未见数据集）上进行了实验，RAF 在客观和主观指标上均取得一致提升。
- 具体地，RAF 训练的 BigVGAN-base 模型在感知质量上优于 LSGAN 训练的 BigVGAN，同时仅使用 12% 的参数。
- 比较研究证实 RAF 能有效增强 GAN vocoders 的域内保真度和对未见场景的泛化能力。

## 一句话评价
RAF 是一个创新且高效的训练框架，通过结合 SSL 模型和相对性配对，显著提升了 GAN vocoders 的性能和泛化能力，同时保持了 GAN 的计算效率优势。

---

## 8. SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns

**作者**: Yongjoon Lee, Jung-Woo Choi
**链接**: [2603.11669](https://arxiv.org/abs/2603.11669)
**分类**: Audio Enhancement | **关键词**: General Speech Restoration, Frequency GLP, Multi-resolution TFDP, Fourier Analysis Network, SEMamba++

# SEMamba++ 论文详细总结

## 核心痛点
- 现有通用语音恢复（GSR）方法在时频双路径（TFDP）处理中，时间与频率特征处理架构相同，但二者特性不同（频率具有全局、局部和周期性模式），导致模型无法有效捕获关键语音特征如频谱周期性。
- 频率特征提取模块（如 Conformer 或 SpatialNet）缺乏局部-全局选择性，且未充分建模频谱周期性，限制了在多种退化场景下的恢复能力。
- 单分辨率 TFDP 处理存在计算开销大（由于长序列处理）和多尺度特征提取机会缺失的问题，影响模型效率和性能。

## 方法创新
- **Frequency GLP**: 提出一个频率特征提取块，并行连接全局周期性模块（GP，基于傅里叶分析网络 FAN 直接处理频率轴以捕获周期性模式）和局部模块（L，使用卷积块处理子带局部特征），通过拼接和点卷积选择信息流，增强对全局、局部和周期性模式的建模。
- **多分辨率并行 TFDP 处理**: 设计多分辨率并行架构，仅在频率轴下采样，保留时间分辨率，并行处理三个频率分辨率，使模型能捕获多样频谱模式，同时提高计算效率（避免单分辨率的计算负担）。
- **可学习映射**: 引入基于 softplus 的可学习映射，分配频率超参数，以利用频率箱的异质特性进一步优化模型性能。

## 实验结果
- 论文摘要报告 SEMamba++ 在多个基线模型（包括 Universe++、ANYENHANCE、CMGAN、SEMamba 等）中实现了最佳性能，同时在计算上保持高效。具体实验细节在截断内容中未完全提供，但创新方法被验证有效。

## 一句话评价
SEMamba++ 通过集成语音特定归纳偏置，创新性地结合 Frequency GLP 和多分辨率并行处理，显著提升了通用语音恢复的准确性和效率，为解决复杂退化场景下的语音恢复问题提供了有力框架。

---

## 9. Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts

**作者**: George Saon, Samuel Thomas, Takashi Fukuda, Tohru Nagano, Avihu Dekel, Luis Lastras
**链接**: [2603.11243](https://arxiv.org/abs/2603.11243)
**分类**: Speech Recognition | **关键词**: Self-Speculative Decoding, Speech-Aware LLM, CTC

## 核心痛点

语音感知语言模型（SLMs）如注意力编码器-解码器模型采用自回归推理，每次生成一个令牌需要LLM的一次前向传递，导致推理速度慢、并行性受限，影响自动语音识别系统的实时性和效率。

## 方法创新

提出自投机解码方法，利用SLM中预训练的CTC编码器作为草稿模型，无需额外训练。过程分三步：
- **CTC解码和验证**：基于CTC输出分布的帧级熵，若所有熵值低于阈值，直接接受贪婪CTC假设为最终输出。
- **SLM验证**：否则，在单次LLM前向传递中验证CTC假设，使用令牌似然性的放松接受准则（如似然高于阈值）。
- **自回归回退**：若验证失败，从最长验证CTC前缀恢复自回归解码。
该方法通过CTC和SLM的互补错误模式提升准确性，并加速推理。

## 实验结果

在九个语料库和五种语言上测试，使用1B参数LLM和440M参数CTC编码器。在HuggingFace Open ASR基准上，实现5.58%的词错误率，逆实时因子提高4.4倍，仅比纯自回归搜索增加12%的相对WER。实验显示，在不同阈值设置下能平衡速度和精度，例如在高效模式下WER略增但推理加速显著。

## 一句话评价

该方法巧妙结合CTC的快速解码和LLM的准确性，通过自投机机制优化了ASR系统的推理效率与性能，为语音识别领域提供了一种实用的加速方案。

---

## 10. Cough activity detection for automatic tuberculosis screening

**作者**: Joshua Jansen van Vüren, Devendra Singh Parihar, Daphne Naidoo, Kimsey Zajac, Willy Ssengooba, Grant Theron, Thomas Niesler
**链接**: [2603.11241](https://arxiv.org/abs/2603.11241)
**分类**: Audio Activity Detection | **关键词**: cough activity detection, tuberculosis screening, transformer models, automatic cough segmentation, XLS-R, AST

# 核心痛点
手动标注咳嗽音频的起始点耗时、费力且存在卫生风险，在临床环境中不可行，阻碍了可扩展的移动健康筛查工具的开发。需要自动检测咳嗽活动以避免人工干预，并确保下游疾病分类模型的准确性。

# 方法创新
提出使用两个预训练的 transformer 模型进行咳嗽活动检测：XLS-R（基于语音训练的 transformer）和音频声谱图 transformer（AST）。创新点包括：
- 应用 transformer 模型于咳嗽检测任务，首次探索其在此领域的潜力。
- 优化 XLS-R，仅使用其前三层，以减少计算和内存需求，适用于智能手机应用。
- 与 logistic regression 基线比较，评估 transformer 模型的性能优势。
- 研究自动提取咳嗽对下游结核病分类模型的影响，对比人工标注的咳嗽输入。

# 实验结果
- XLS-R 在测试集上实现平均精度 0.96 和接收器操作特征曲线下面积 0.99。
- 仅使用前三层的 XLS-R 配置在平均精度上分别优于 AST 和 logistic regression 基线 9% 和 27%。
- 下游 TB 分类模型使用 XLS-R 自动提取的咳嗽输入表现良好，接近基于人工标注咳嗽的模型性能。
- 数据集来自南非和乌干达的社区医疗中心，包含背景噪音，增强了模型的实用性。

# 一句话评价
预训练的 transformer 模型在咳嗽活动检测中表现卓越，有效减少人工依赖，集成到结核病筛查工具具有可行性。

---

## 11. Can LLMs Help Localize Fake Words in Partially Fake Speech?

**作者**: Lin Zhang, Thomas Thebaud, Zexin Cai, Sanjeev Khudanpur, Daniel Povey, Leibny Paola García-Perera, Matthew Wiesner, Nicholas Andrews
**链接**: [2603.11205](https://arxiv.org/abs/2603.11205)
**分类**: Speech Forensics | **关键词**: LLMs, fake word localization, partially fake speech, speech LLM, editing patterns

# 详细总结

## 核心痛点
部分虚假语音（partially fake speech）指仅特定单词被编辑的语音，其检测和定位虚假区域极具挑战性，因为编辑可能仅改变语义，而现有方法在泛化到不同编辑风格时表现不佳。

## 方法创新
本研究提出一种语音LLM（Speech LLM）模型，通过下一个token预测来定位虚假单词。创新点包括：构建基线Align模型（结合ASR和帧级检测器），并探讨三种输入模态的Speech LLM：音频-only（SLM-A）、音频+转录（SLM-AT）和转录-only（LLM-T），以分析模型在不同场景下的行为。

## 实验结果
在PartialEdit（PE）和AV-Deepfake1M（AV1M）数据集上的实验表明：当转录可用时（SLM-AT），模型在WordF1指标上表现最佳（PE: 90.79%, AV1M: 97.51%）。跨域测试显示模型过度依赖数据集特定的编辑模式（如极性替代），泛化能力有限（例如，从PE训练到AV1M测试时WordF1仅为12.03%）。

## 一句话评价
该论文系统探索了LLM在部分虚假语音定位中的潜力，并揭示了模型依赖的编辑模式，为未来提高泛化能力奠定了基础。

---

## 12. Resurfacing Paralinguistic Awareness in Large Audio Language Models

**作者**: Hao Yang, Minghan Wang, Tongtong Wu, Lizhen Qu, Ehsan Shareghi, Gholamreza Haffari
**链接**: [2603.11947](https://arxiv.org/abs/2603.11947)
**分类**: Audio Language Models | **关键词**: Large Audio Language Models, Paralinguistic Awareness, Layer-wise Analysis, Fine-Tuning, Child Safety

# 论文总结

## 核心痛点
当前大型音频语言模型（LALMs）在与人交互时，通常忽略语音中的副语言线索（如年龄、性别、情绪），只基于查询内容响应。这导致同理心交互减弱，并引发儿童安全问题，例如模型可能为儿童用户提供不适合的指导，如电气安全等场景。

## 方法创新
- 引入五种层-wise分析，共同识别副语言层和语义理解层，通过探测实验发现早期层（如0-6层）保留较强副语言信号，而语义理解在后续层占主导。
- 提出副语言增强微调（PE-FT）协议，包括选择性层微调（针对副语言层）和辅助双级分类头，以整合副语言信号与语义理解。
- 提出新评估指标：PA-score（副语言感知分数）和PA-rate（副语言感知率），作为标准评估范式。

## 实验结果
- 在Qwen2.5-Omni和Kimi-Audio模型上实验，PE-FT协议有效提升了模型在年龄、性别和情绪三个副语言类别的感知性能，甚至超越全层微调策略。
- 缓解了儿童安全问题，模型能根据用户年龄生成适当响应，减少了潜在风险。

## 一句话评价
该研究通过创新的层分析和微调协议，显著增强了LALMs的副语言感知能力，提升了模型的安全性和交互同理心，具有重要应用价值。

---

## 13. AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style

**作者**: Joonyong Park, Jerry Li
**链接**: [2603.11482](https://arxiv.org/abs/2603.11482)
**分类**: Speech Evaluation | **关键词**: Speech evaluation, Preference-based ranking, Anime-likeness, Self-supervised learning, Voice quality

### 核心痛点
评估动漫风格语音缺乏标准化的客观指标，依赖成本高的主观判断，且动漫风格没有共享的绝对尺度，使传统平均意见分（MOS）协议不可靠。

### 方法创新
提出AnimeScore，一个基于偏好的框架，通过成对排名自动评估动漫风格。收集15,000个成对偏好判断和自由形式描述，分析声学特征；使用自监督学习（SSL）基础模型训练排名模型，超越手工艺特征上限。

### 实验结果
手工艺声学特征达到69.3% AUC上限，而SSL基础模型（如掩码预测表示）达到90.8% AUC，接近人类比较判断。数据集公开可用，支持快速模型筛选和基于人类反馈的强化学习（RLHF）优化。

### 一句话评价
该工作为动漫风格语音评估提供了首个实用的自动化框架和数据集，显著提升评估效率和模型优化能力。

---

## 14. Continued Pretraining for Low-Resource Swahili ASR: Achieving State-of-the-Art Performance with Minimal Labeled Data

**作者**: Hillary Mutisya, John Mugane
**链接**: [2603.11378](https://arxiv.org/abs/2603.11378)
**分类**: Speech Recognition | **关键词**: Automatic Speech Recognition, Low-Resource Languages, Continued Pretraining, Swahili, African Languages

# 论文总结：Continued Pretraining for Low-Resource Swahili ASR

## 核心痛点
斯瓦希里语作为非洲广泛使用的语言（超过1亿使用者），与其他非洲语言一样，面临高质量标注语音数据稀缺的挑战。高资源语言如英语拥有大量专业转录数据，而低资源语言如斯瓦希里语必须用有限标注数据实现竞争性自动语音识别（ASR），这阻碍了服务于非洲语言社区的语音技术发展。

## 方法创新
本研究提出一种持续预训练（CPT）方法，结合未标注音频和有限标注数据，用于低资源斯瓦希里语ASR。具体方法包括：
1. **伪标签CPT**：使用基线模型（wav2vec2-bert-2.0）对未标注音频生成伪标签（置信度>75%），然后进行持续预训练。
2. **监督微调**：在伪标签CPT后，使用有限标注数据（5K或20K样本）进行监督微调。
3. **训练管道**：包括标签模型训练、伪标签生成、CPT和监督微调三个阶段，使用保守超参数防止灾难性遗忘。

## 实验结果
- **主要结果**：在Common Voice斯瓦希里语数据集上，使用20K标注样本结合CPT，达到3.24%词错误率（WER），比基线（无CPT的50K样本模型，17.71% WER）相对改进81.7%。
- **与基准对比**：超越之前最佳学术系统（XLS-R的8.3% WER），相对改进61%。
- **数据尺度**：5K样本配置达到10.89% WER（相对改进38.5%），20K样本配置达到3.24% WER，表明CPT在有限标注数据下显著提升性能。
- **贡献**：为低资源语言提供了具体数据要求（~20K样本，~11小时标注数据）和可复制方法。

## 一句话评价
该方法通过伪标签持续预训练有效解决了斯瓦希里语ASR的数据稀缺问题，以最小标注数据实现最先进性能，为其他低资源语言提供了实用路径。

---

## 15. Fair-Gate: Fairness-Aware Interpretable Risk Gating for Sex-Fair Voice Biometrics

**作者**: Yangyang Qu, Todisco Massimiliano, Galdi Chiara, Evans Nicholas
**链接**: [2603.11360](https://arxiv.org/abs/2603.11360)
**分类**: Fairness in Speaker Verification | **关键词**: voice biometrics, speaker verification, fairness, sex bias, risk extrapolation

# 详细总结

## 核心痛点
语音生物识别系统（特别是说话者验证）在性别上存在系统性性能差距，即使整体验证准确率高。这种差距源于两个机制：1. **人口统计快捷学习**：模型训练中利用性别与说话者身份之间的虚假相关性作为捷径；2. **特征纠缠**：性别相关的声学变化与身份线索重叠，难以在不降低说话者鉴别能力的情况下移除。这导致在共享决策阈值下，不同性别组的错误率不平等。

## 方法创新
提出**Fair-Gate**，一个公平感知的可解释风险门控框架。主要创新包括：
1. **风险外推（Risk Extrapolation, REx）**：在代理性别组间惩罚说话者分类风险的变化，以减少组间捷径依赖。
2. **局部互补门控**：通过软路由掩码将中间特征分配到身份分支和性别分支，保持特征维度不变，提供可解释性（可检查哪些特征被分配到身份或性别路径）。
3. **综合训练目标**：结合说话者分类、对抗性别分类、嵌入去相关、门控正则化等损失函数，优化效用-公平权衡。

## 实验结果
- **数据集和协议**：在VoxCeleb2上训练，在VoxCeleb1上评估，使用Vox1-O（原始测试列表）、Vox1-E（扩展试验集）和Vox1-H（硬协议，匹配国籍和性别的冒名者）协议。
- **结果**：Fair-Gate改善了效用（验证性能）与公平性（性别组间错误率平等）的权衡，在挑战性评估条件下（如共享全局阈值）产生了更性别公平的自动说话者验证（ASV）性能。

## 一句话评价
该工作通过因果分析和创新框架，有效解决了说话者验证中的性别偏见问题，同时保持了高验证性能，为公平语音生物识别提供了实用方案。

---

## 16. V2A-DPO: Omni-Preference Optimization for Video-to-Audio Generation

**作者**: Nolan Chan, Timmy Gang, Yongqian Wang, Yuzhe Liang, Dingdong Wang
**链接**: [2603.11089](https://arxiv.org/abs/2603.11089)
**分类**: Video-to-Audio Generation | **关键词**: Video-to-Audio, Direct Preference Optimization, Human Preference Alignment, Flow Matching, Curriculum Learning

### 核心痛点
现有视频到音频生成（V2A）模型存在以下主要问题：风格控制受限于训练数据，缺乏灵活性；美学质量难以通过显式奖励建模评估；缺乏综合评分系统来整体评估语义一致性、时间对齐和感知质量。

### 方法创新
论文提出V2A-DPO框架，包含三个核心创新：
1. **AudioScore**：一个基于人类偏好对齐的综合评分系统，评估生成音频的语义一致性、时间对齐和感知质量。
2. **自动化偏好对数据生成**：利用AudioScore驱动管道，结合少量人工标注数据，生成大规模偏好对用于DPO优化。
3. **课程学习驱动的DPO优化**：针对基于流的生成模型，通过分阶段训练（从简单到复杂偏好对）提升优化效果。

### 实验结果
在VGGSound数据集上的实验表明，使用V2A-DPO优化的Frieren和MMAudio模型在多个指标上优于使用DDPO优化的版本和预训练基线。具体改进包括：IS提升1.81绝对值（10.4%相对），IB-score提升0.86绝对值（2.6%相对），DeSync降低0.09绝对值（20.5%相对）。DPO优化的MMAudio在多个指标上达到SOTA性能，超越已发表的V2A模型。

### 一句话评价
该论文通过创新地将直接偏好优化应用于视频到音频生成，有效解决了人类偏好对齐的挑战，显著提升了生成音频的质量和综合评估。

---

