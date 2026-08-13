# Arxiv Daily Deep Report - 2026-06-24

**来源**: https://arxiv.org/list/eess.AS/recent
**篇数**: 23
---

## 1. A Methodology for Characterizing Underwater Radiated Noise from Submerged Electric Vehicles in a Coastal Environment: An AUV Test Case

**作者**: Mark Shipton, Amir Boag, Roee Diamant
**链接**: [2606.24813](https://arxiv.org/abs/2606.24813)
**分类**: Underwater Acoustics, Passive Acoustic Characterization | **关键词**: Underwater radiated noise, Submerged electric vehicles, Autonomous underwater vehicle, Tonal noise, Source-level estimation, Passive acoustics

## 核心痛点
现有水下辐射噪声（URN）标准（如ISO 17208-1、ANSI/ASA S12.64）主要针对水面船舶，无法适用于水下电动车辆（SEV），因其辐射特征以窄带谐波和调制分量为主，而非宽带空化噪声，且在浅海环境中受背景噪声、传播效应和方向依赖性的影响，难以表征。

## 方法创新
提出一个八步法框架，结合校准的经过测量、同步车辆元数据（速度、深度等）、背景噪声评估、子系统导向的谱解释和传播校正的源级估计。核心在于通过窄带和时频分析解析SEV特有的电机驱动相关音调，而非宽带方法。

## 实验结果
在A18D AUV的沿海测试中，观测到5.56、11.1和22.2 kHz附近的驱动相关音调群，谐波结构延伸至105 kHz。源相关音调PSD估计范围为77–120 dB re 1 µPa²/Hz @ 1m。

## 一句话评价
该工作填补了SEV水下噪声标准化表征方法的空白，其子系统分析和高频扩展（>105 kHz）显著优于以往局限于5–16 kHz的研究。

---

## 2. Perceptual Evaluation of Higher-Order Ambisonic Codecs on Both Synthetic Mixing and Native Recordings

**作者**: Adrien Llave, Grégory Pallone, Jérôme Daniel
**链接**: [2606.24661](https://arxiv.org/abs/2606.24661)
**分类**: Audio Coding / Spatial Audio | **关键词**: Higher-Order Ambisonics, IVAS, spatial audio coding, perceptual evaluation, inter-channel correlation

# Perceptual Evaluation of Higher-Order Ambisonic Codecs

## 核心痛点
高阶Ambisonics (HOA) 格式（如3阶需16通道）在传输和存储时占用极高带宽（如12,288 kbps），需要高效的、低延迟的编解码器以满足AR/VR等实时通信场景。

## 方法创新
本文评估了最新的3GPP IVAS编解码器（场景音频模式，SBA）与多单声道方法（EVSx16，即独立对每通道应用EVS）的感知质量。IVAS结合SPAR和DirAC算法，通过提取低时间分辨率空间参数并传输有限数量的传输通道（TCs），利用通道间相关性实现高效压缩。

## 实验结果
- 主观测试（MUSHRA）表明，在相同或更低比特率下，IVAS性能优于EVSx16。
- IVAS对由有限平面波合成的信号（高通道间相关性）尤为有效；而EVSx16对空间扩散内容（低相关性）表现更好。
- 随着比特率降低，IVAS对合成内容的优势更明显。

## 一句话评价
IVAS编解码器利用HOA通道相关性在低比特率下实现高效压缩，但其性能依赖于内容类型，需要根据应用场景选择编码策略。

---

## 3. SphereVBx: Spherical Variational Bayes Clustering for Simplified EEND-VC Diarization

**作者**: Petr Pálka, Jiangyu Han, Prachi Singh, Marc Delcroix, Naohiro Tawara, Lukáš Burget
**链接**: [2606.24528](https://arxiv.org/abs/2606.24528)
**分类**: Speaker Diarization | **关键词**: Speaker diarization, EEND-VC, VBx, T-PSDA, variational Bayes clustering, von Mises–Fisher distribution

## 核心痛点
现有说话人日志方法（如VBx）使用高斯PLDA后端，不适用于现代长度归一化且基于角度边界的球面嵌入；EEND-VC框架的聚类阶段依赖多个启发式步骤（如过滤短片段、余弦重分配），不够简洁。

## 方法创新
- 提出SphereVBx，用Toroidal Probabilistic Spherical Discriminant Analysis (T-PSDA)替代VBx中的PLDA，构建基于von Mises–Fisher混合分布的变分贝叶斯聚类框架。
- 参数无关变体SphereVBx-PF：通过设置特定参数（d=D, κ_b=0, κ_w=1）使模型退化为余弦相似度评分，无需预训练参数。
- 引入可靠性权重（基于持续时间）替代硬性过滤，保留所有嵌入但弱化不可靠样本的影响。
- 提出Multi-Stream SphereVBx，直接通过概率模型融入窗口内“cannot-link”约束，无需后处理重分配。
- 简化的GMM形式代替HMM，提升推理速度。

## 实验结果
在多个标准说话人日志基准上，SphereVBx在级联和EEND-VC流水线中均提升聚类准确性，并在EEND-VC框架中取得与基线相当或更优性能，同时显著简化聚类阶段（减少启发式步骤）。

## 一句话评价
SphereVBx通过球面贝叶斯聚类为EEND-VC提供了统一、简洁且性能优异的替代方案。

---

## 4. A Multi-Stage Separation-and-Classification Framework Guided by Complementary Acoustic-to-Semantic Clues

**作者**: Younghoo Kwon, Junwoo Park, Han Yin, Jung-Woo Choi
**链接**: [2606.24512](https://arxiv.org/abs/2606.24512)
**分类**: Audio Source Separation and Classification | **关键词**: Audio Source Separation, Audio Classification, Duration-Based Augmentation, Temporal-FiLM, Self-Guided Refinement, DCASE 2026, Spatial Semantic Segmentation

## 论文总结

### 核心痛点
- **分类模型效率低**：微调预训练模型（M2D）导致表示能力退化，且将分离波形转换为幅度谱丢失相位和细粒度频率信息。
- **语义线索融合方式粗糙**：传统SEC将one-hot向量与预训练嵌入简单相加，导致信息稀释；且预训练嵌入时间分辨率粗（16倍下采样），无法捕捉细粒度时变动态。
- **打击乐类分类性能差**：短暂瞬态样本（如鼓声）缺乏时间上下文，常被误分类为静音。

### 方法创新
1. **多阶段自引导框架**：阶段1（线索推导）：DeFT-Mamba-USS分离多通道混合，DPC分类。阶段2（引导提取）与阶段3（迭代精炼）：DeFT-Mamba-TSE利用前级输出的波形（enrollment clue）、one-hot类别（class clue）以及AF-Whisper的细粒度语义嵌入逐步精炼提取。
2. **细粒度语义条件化**：采用AudioFlamingo-Whisper编码器提取20ms帧级嵌入，通过独立的Temporal-FiLM层注入DeFT-Mamba-TSE，避免与one-hot信息的稀释。
3. **时长增强**：对打击乐类，在训练时将短样本（<4s）与长样本（>=4s）随机混合，增加瞬态事件的时间上下文。
4. **类别特定静默阈值优化**：在验证集上对每个类别调整静默阈值，最大化CAPI-SDRi，减少误分类为静音导致的惩罚。

### 实验结果
- **官方测试集**：CAPI-SDRi 15.51 dB（提升7.02 dB），混合准确率71.09%（提升10.38%p），源准确率78.62%（提升8.22%p）。
- **数据改进**：替换语音为VCTK高保真语料库；补充吸尘器类来自AudioSet-2M的高质量子集。
- **损失函数**：多任务损失包含SA-SDR分离损失、ArcFace分类损失和BCE静默损失。

### 一句话评价
该论文通过多阶段自引导框架和细粒度语义条件化，显著提升音频分离与分类的联合性能，在DCASE 2026 S5任务上大幅超越基线。

---

## 5. The effect of micro-changes in the pluck trajectory on the sound of an acoustic guitar

**作者**: Marek Pluta, Jan Jasiński, Daniel Tokarczyk, Julia Grygiel
**链接**: [2606.24356](https://arxiv.org/abs/2606.24356)
**分类**: N/A | **关键词**: 

# Summary

## Core Problem
Existing plucking mechanisms lack the precision and flexibility to study sub-millimeter changes in plucking trajectory, leaving the effect of microscopic geometric variations on guitar sound largely unexplored.

## Methodological Innovation
- Used a state-of-the-art Cartesian-coordinate robotic plucker with 0.04 mm precision, enabling 192 µm steps in plucking depth.
- Measured six different plectrum materials (e.g., nylon, celluloid, Delrin) to separate the influence of pick properties.
- Recorded 10 repetitions per condition (8 plectra × 6 depths = 480 plucks) in an anechoic chamber with four microphones.
- Analyzed loudness, timbre (spectral centroid, brightness), inharmonicity, noisiness, and decay evolution.

## Key Experimental Results
- At very low attack depth (position I), the string is barely excited, producing a weak, altered sound.
- As depth increases, loudness rises, inharmonicity and noise decrease, and timbre becomes fuller in low frequencies and rougher.
- The threshold depth for full excitation depends on plectrum material (stiffer picks require deeper attack).
- The effect saturates beyond a certain depth, beyond which further changes are minimal.

## One-sentence Evaluation
This paper provides the first high‑resolution experimental data on how micrometer‑scale plucking depth variations systematically affect guitar tonal qualities, highlighting the necessity of precise mechanical repeatability in guitar testing.

---

## 6. Digital Revival: Acoustic Documentation and Digital Reactivation of Historical Woodwind Instruments

**作者**: Lior Arbel, Itai Weissman
**链接**: [2606.24216](https://arxiv.org/abs/2606.24216)
**分类**: Audio Processing for Cultural Heritage | **关键词**: digital revival, historical woodwind instruments, acoustic documentation, digital reactivation, EWI, physical modelling, spectral analysis, non-invasive characterization

# Digital Revival: Acoustic Documentation and Digital Reactivation of Historical Woodwind Instruments

## 核心痛点
历史木管乐器因年代久远、结构脆弱或保存限制而无法演奏，其声音无法被公众、研究人员和演奏者获取。博物馆中的大量乐器处于“沉默”状态，文化遗产的声学维度被忽视。

## 方法创新
提出 Digital Revival 项目，采用非侵入式声学测量（输入阻抗、几何扫描）和物理建模，结合高分辨率采样与 EWI（电子吹管）控制器，将历史乐器声音数字化为可演奏的数字乐器。主要方法包括：
- 对于可演奏乐器（如Haka长笛）：在受限条件下高保真采样，结合物理建模（Respiro插件）和攻击音层，构建三层数字乐器。
- 对于不可演奏乐器（如Warder长笛）：通过几何成像（CT扫描）获取管体数据，使用多模态波导理论物理建模，并基于3D打印复制品进行特征提取。
- 数字乐器通过Kontakt实现，支持EWI实时演奏，保留乐器“声音DNA”的同时创造新的音乐身份。

## 实验结果
- Haka长笛（约1680年）：原始乐器在2、4、6、8次谐波处能量高于现代复制品，10次谐波后接近底噪。
- Warder长笛（约1540年，沉船出水）：原始乐器二次谐波能量更强，但三次及四次谐波弱于复制品，四次谐波后能量接近底噪。
- 数字乐器成功扩展至五八度（C1-C6），在音乐会中实际使用，音色具有历史特征。

## 一句话评价
该工作通过声学测量、物理建模与数字控制器的系统性融合，成功“复活”了历史木管乐器的声音，为文化遗产声学保护与创造性再利用提供了可复用的方法论。

---

## 7. Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training

**作者**: Wonchul Shin, Inyong Choi, Kyogu Lee
**链接**: [2606.24164](https://arxiv.org/abs/2606.24164)
**分类**: EEG-guided Target Speech Extraction | **关键词**: target speech extraction, auditory attention decoding, EEG, shortcut learning, contrastive learning, cross-trial generalization

## 核心痛点
现有端到端EEG引导目标语音提取（TSE）模型在试验内（within-trial）评估中表现优异，但在跨试验（cross-trial）泛化中失败。原因是模型容易利用试验特定的EEG模式（如时间自相关、缓慢漂移）作为捷径，而非关注与注意力相关的神经信号，导致在未见过的试验中性能急剧下降。

## 方法创新
提出TRUST-TSE，一种两阶段训练框架：
1. **阶段1：对比预训练** - 使用注意说话人负采样（attended-speaker negative sampling），即从同一说话人的其他片段中抽取负样本，迫使EEG编码器学习细粒度的EEG-语音对齐，抑制试验身份线索。
2. **阶段2：置信度加权提取** - 基于EEG-源相似度计算置信度权重，并加权SI-SDR损失，引导提取器关注与EEG嵌入对齐良好的样本。

## 实验结果
在KUL和DTU数据集上，TRUST-TSE在严格跨试验协议下显著优于端到端基线（如NeuroHeed），展示了可靠的跨试验泛化能力。

## 一句话评价
本文系统分析了跨试验泛化瓶颈，并提出简洁有效的两阶段训练方案，为实用化脑控听觉技术提供了新思路。

---

## 8. Progressive Alignment Objectives for Aligner-Encoder based ASR

**作者**: Jaeyong Lee, Masato Mimura, Takafumi Moriya
**链接**: [2606.24147](https://arxiv.org/abs/2606.24147)
**分类**: Speech Recognition | **关键词**: Aligner-Encoder, InterAligner, InterCTC, 渐进对齐, 语音识别

## 核心痛点
Aligner-Encoder 模型中的对齐仅在编码器顶层急剧形成，导致训练过程敏感且对长语句的识别性能严重下降。

## 方法创新
提出 InterAligner，通过在中间层（第15层）添加辅助对齐目标，使用更细粒度的 token 序列（BPE 256），并在早期层（第12层）添加中间 CTC 损失（InterCTC），使得对齐能够渐进地在深度方向上形成，从而缓解晚层对齐瓶颈。

## 实验结果
- 在 LibriSpeech 上：最终 Aligner 基线 WER 5.0/7.8（test-clean/other），+InterCTC 改进至 3.4/6.0，+InterAligner 进一步降至 3.1/5.6。
- 长语句（>21s）上提升显著：test-clean 从 17.0 降至 11.6，test-other 从 18.0 降至 13.5。
- Common Voice 英文上也验证了类似改进（从 12.4 降至 10.9）。

## 一句话评价
通过渐进中间对齐目标有效提升了 Aligner-Encoder 的鲁棒性和长语句识别性能。

---

## 9. Evaluation of Headrest-Integrated Loudspeakers for Enhanced Spatial Audio Immersion in Automotive Cabins

**作者**: Martin Wolters, Jacobo Giralt, Harald Mundt, Arijit Biswas
**链接**: [2606.24146](https://arxiv.org/abs/2606.24146)
**分类**: Audio Enhancement | **关键词**: Automotive spatial audio, headrest loudspeakers, binaural rendering, HRTF processing, Bradley-Terry-Luce model

## 核心痛点
传统汽车音响系统在提供沉浸式音频体验时，受限于扬声器布局，难以在车内创建个人声区，且对乘客干扰较大。头枕集成扬声器虽有50年历史，但未成为标准配置，其在沉浸式音频中的潜力尚未被充分验证。

## 方法创新
- 在实验室车辆（Volvo XC60）中配置三种渲染方案：离散7.1.4（全车厢）、7.1.4+头枕（全车厢增强）、仅前声场+头枕（简化布局）。
- 对头枕通道应用双耳化处理（HRTF/BRIR）以补偿物理位置，模拟环绕和高度声源方向。
- 采用强迫选择配对比较实验，评估整体偏好、响度、空间感、频谱自然度、清晰度五个属性。
- 使用Bradley-Terry-Luce概率选择模型对偏好数据进行排序，并计算Pearson相关系数分析属性与偏好的关联。

## 实验结果
- 头枕增强配置（全车厢+头枕）在空间感和整体偏好上显著优于纯全车厢配置。
- 简化布局（前声场+头枕）在保持合理空间质量的同时，提供了个人声区隔离优势。
- 响度匹配后（差异<0.5 LKFS），头枕配置未引入明显音色失真。
- 统计显著性通过二项检验验证。

## 一句话评价
该研究通过严格的主观实验证明了头枕集成扬声器结合双耳处理可有效增强汽车沉浸式音频体验，为下一代车载音响设计提供了有力依据。

---

## 10. Joint Learning of Covariance Estimation and White Noise Gain for Robust MVDR Beamforming

**作者**: Yongyi Deng, Hanchen Pei, Jianbo Ma, Gongping Huang, Jingdong Chen, Jacob Benesty
**链接**: [2606.24137](https://arxiv.org/abs/2606.24137)
**分类**: Audio Enhancement | **关键词**: MVDR beamforming, white noise gain, robustness, deep neural network, speech enhancement

# 论文总结

## 核心痛点
传统MVDR波束形成器对麦克风自噪声和阵列失配敏感，现有的WNG约束或对角加载方法依赖固定、手动调节的阈值，无法适应未知或时变的声学环境，导致性能次优。

## 方法创新
提出一种数据驱动的MVDR框架，通过双分支神经网络联合估计时频噪声掩码（用于协方差矩阵估计）和频率相关的WNG阈值（用于鲁棒性控制）。将可微分的WNG约束MVDR层嵌入网络，实现端到端优化。WNG阈值不再作为固定超参数，而是通过数据学习得到。

## 实验结果
实验表明，在语音质量和可懂度指标上，所提方法一致优于固定WNG阈值的传统MVDR方法，尤其在阵列失配条件下优势明显。

## 一句话评价
提出首个端到端学习WNG约束和噪声协方差的鲁棒MVDR框架，实现了自适应鲁棒性与指向性权衡。

---

## 11. DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration

**作者**: Youran Ni, Shihong Tan, Yuzhu Wang, Gongping Huang
**链接**: [2606.24127](https://arxiv.org/abs/2606.24127)
**分类**: Audio Enhancement / Music Source Restoration | **关键词**: Music Source Restoration, Generative-Regression Cascade, DTT-BSR, Demucs, MMSNR, FAD

# 论文总结：DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration

## 核心痛点
现有音乐源恢复（MSR）方法在信号重建准确度与语义一致性之间存在权衡，多阶段系统（如X-LANCE）虽语义拟合好但波形重建精度低，单阶段系统（如DTT-BSR）同样面临MMSNR（多梅尔信噪比）有限的问题。

## 方法创新
提出两阶段级联系统DTT-BSR+：
1. **第一阶段（生成式分离）**：采用基于GAN的DTT-BSR分离器，对退化混合信号进行语义分布拟合，输出与干净源分布一致的估计。
2. **第二阶段（波形重建）**：使用改进的Demucs网络（Demucs-L），去除BLSTM瓶颈以聚焦局部波形重建，并用时间域L1损失和多分辨率STFT损失联合优化，提升波形级精度。
该设计将分布拟合与信号重建解耦，避免两者冲突。

## 实验结果
- 在所有8个stem（人声、吉他、键盘、合成器、贝斯、管弦乐、鼓、打击乐）上，DTT-BSR+的MMSNR均优于单阶段DTT-BSR，尤其贝斯（2.49→9.29dB）、鼓（2.24→8.79dB）、人声（3.34→6.72dB）提升显著。
- 在5个stem（人声、吉他、合成器、贝斯、鼓）上超过当前最优系统X-LANCE MSR。
- 通过FAD（Fr\u00e9chet Audio Distance）分解揭示：信号重建精度提升不一定带来FAD改善，存在隐式权衡，且FAD退化主要由语义均值偏移（D\u03bc）而非方差变化（D\u03a3）导致。

## 一句话评价
提出了一种有效的生成-回归级联框架，在音乐源恢复任务上实现了信号重建与语义一致性的较好平衡，达到领先性能。

---

## 12. Autoencoder based optimized SSL representations: Complexity Minimization and improved Dysarthric ASR

**作者**: Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo, Shrikanth Narayanan, Sudarsana Reddy Kadiri
**链接**: [2606.24088](https://arxiv.org/abs/2606.24088)
**分类**: Dysarthric Speech Recognition | **关键词**: dysarthric speech recognition, self-supervised learning, autoencoder, bottleneck features, ASR, Kaldi, TORGO dataset, Wav2Vec2, HuBERT, Data2Vec

## 核心痛点
高维自监督学习（SSL）特征（如Wav2Vec2、HuBERT、Data2Vec的1024维输出）导致计算复杂度高，训练时间长，尤其在资源受限环境中难以部署。同时，构音障碍语音因发音缓慢、不清、多变，传统ASR系统性能不佳。

## 方法创新
提出SSL-AutoEncoder（SSL-AE）瓶颈方法，通过自编码器将高维SSL特征压缩为低维瓶颈表示（实验维度k=512,256,128,64,32,13），在保持关键语音信息的同时降低模型复杂度。自编码器采用无监督逐批训练（每批256帧，每批20轮），仅保留编码器用于特征提取，解码器用于训练。将压缩后的瓶颈特征输入Kaldi DNN-HMM ASR流水线，降低训练时间和计算成本。

## 实验结果
在TORGO构音障碍语音数据集上评估，包含15位说话人（8位构音障碍，7位正常），按严重程度分为低、中、高三组及对照组。采用四种训练-测试配置（Sys0-Sys3）。主要结果：
- **MFCC基线**：平均WER 55.89%。
- **零样本SSL解码**：Wav2Vec2最佳平均WER 60.35%。
- **微调Wav2Vec2**：平均WER 40.48%，但需约30小时训练和11 GiB GPU。
- **提出的SSL-AE方法**：在保持或降低WER的同时，训练时间减少8倍（相比SSL基线），效率显著提升。

## 一句话评价
通过自编码器瓶颈压缩SSL特征，在构音障碍ASR中实现了计算复杂度和识别性能的优化平衡，为资源受限场景提供高效方案。

---

## 13. A Fusion-Aware Two-Stage Framework for Mispronunciation Detection and Diagnosis in Low-Resource Modern Standard Arabic

**作者**: Jing Yang, Shuqing Zhang, Yongyi Deng, Pan Li, Ting Dang, Gongping Huang, Jingdong Chen, Jacob Benesty
**链接**: [2606.24086](https://arxiv.org/abs/2606.24086)
**分类**: Speech Recognition | **关键词**: Mispronunciation Detection and Diagnosis, Modern Standard Arabic, Two-stage training, Causal Temporal Convolutional Networks, Ensemble inference, N-gram rescoring

## 核心痛点
低资源现代标准阿拉伯语（MSA）中，数据稀缺和合成-真实语音域差距限制了发音错误检测与诊断（MDD）的性能。

## 方法创新
提出一种两阶段端到端框架：
1. **混合架构**：将大规模多语言预训练编码器（wav2vec2-XLS-R）与因果扩张时序卷积网络（TCN）结合，保留细粒度语音变化。
2. **分层两阶段训练**：第一阶段在大量母语和合成数据上学习通用声学-音素映射；第二阶段在少量真实学习者语音上微调，弥合域差距。
3. **多样性感知集成推理**：在多检查点之间构建混淆网络（CN），并结合修正Kneser-Ney N-gram语言模型重评分，提升预测稳定性。

## 实验结果
在QuranMB.v2测试集上，音素级F1分数达0.7201，相对基线（0.4414）提升63.1%，在Interspeech 2026 IqraEval.2挑战中排名第一。

## 一句话评价
该框架通过两阶段训练与集成推理，在低资源阿拉伯语MDD任务上取得了SOTA性能。

---

## 14. Comparative Reasoning: Making an Audio Language Model Better at Comparing Emotions

**作者**: Abinay Reddy Naini, Jaeyeon Kim, Chao-Han Huck Yang, Shinji Watanabe, Carlos Busso
**链接**: [2606.24082](https://arxiv.org/abs/2606.24082)
**分类**: Speech Emotion Recognition | **关键词**: Large audio-language models, speech emotion recognition, emotion reasoning, preference learning, comparative reasoning

## 论文总结

### 核心痛点
现有大型音频语言模型（LALM）在跨音频比较推理方面能力不足，尤其是在情感比较任务中，无法提供可解释的决策依据。传统序数情感识别方法仅依赖标注标签，缺乏显式推理过程。

### 方法创新
提出了推理引导的序数语音情感识别框架：
1. 结合语义音频描述（由Qwen3-Omni-Captioner生成）和GeMAPS声学特征（提取18个低层描述符的均值和标准差，离散化为定性等级），构建比较推理轨迹。
2. 采用监督微调（SFT）和直接偏好优化（DPO）进行训练，其中DPO使用正确/错误答案对应的推理轨迹构建偏好对。
3. 使用大型推理模型生成结构化推理轨迹（少于5句），确保可解释性和准确性。

### 实验结果
- 仅需传统序数SER系统5%的训练数据即可提升偏好预测性能。
- 引入推理轨迹显著提高了模型决策的可解释性。

### 一句话评价
通过结合语义与声学特征的推理轨迹，首次将LALM应用于可解释的情感比较推理，数据效率高且效果显著。

---

## 15. Audio--Image Alignment as a Continued-Pretraining Stage Improves Low-Resource ASR

**作者**: Sujith Pulikodan, Nihar Desai, Prasanta Kumar Ghosh
**链接**: [2606.24080](https://arxiv.org/abs/2606.24080)
**分类**: Speech Recognition | **关键词**: Low-resource ASR, audio-image alignment, representation learning, multimodal learning, contrastive learning

### 核心痛点
低资源语言自动语音识别（ASR）由于缺乏高质量转录数据，面临性能瓶颈。传统预训练-微调范式依赖大量标注语音-文本对，而收集准确转录成本高昂。

### 方法创新
提出在自监督预训练和监督ASR微调之间引入**音频-图像表示对齐阶段**，利用无需转录的音频-图像对（来自Vaani数据集）进一步适应预训练音频编码器。具体包括：
- 使用预训练视觉编码器（SigLIP2 Base/Large、Qwen3-VL）提取图像特征，固定视觉编码器。
- 音频编码器（FastConformer）通过对比学习（SigLIP sigmoid loss）对齐音频和图像表示，引入对齐头（MLP）和注意力池化。
- 三种配置：SigLIP（单向量余弦相似度）、SigLIP-MT（多查询注意力池化，16 tokens）、Qwen-MT（类似，但视觉侧top-k tokens）。
- 对齐后，音频编码器与混合CTC-TDT解码器联合微调于转录数据。

### 实验结果
- 在Vaani和FLEURS数据集上评估，使用WER指标。
- 与直接微调基线（无对齐阶段）相比，所有对齐变体均一致降低WER，统计显著（p<0.05）。
- 最好配置（SigLIP-MT）在低资源语言上提升更明显。

### 一句话评价
本文巧妙利用跨模态对齐作为转录无关的预训练增强，简单有效，为低资源ASR提供新思路。

---

## 16. A Variational-Flow Analysis of StoRM under Noise-Power Mismatch

**作者**: Shuubham Ojha
**链接**: [2606.24035](https://arxiv.org/abs/2606.24035)
**分类**: Speech Enhancement | **关键词**: diffusion model, StoRM, kink, variational-flow analysis, speech enhancement, noise-power mismatch

## 核心痛点
扩散语音增强模型（如StoRM）在噪声功率失配下，SI-SDR退化曲线在训练噪声幅度处出现尖锐的非光滑过渡（“kink”），但其成因不明。

## 方法创新
提出路径变分流分析，将输出对噪声缩放参数的敏感性分解为连续矩阵值泛函K(M)与预测器敏感性的乘积，并证明该kink定位到预测器阶段，且给出充要条件。将分析扩展到离散Euler-Maruyama采样器。

## 实验结果
论文为假设验证设计了完整的实验程序，包括五个实证支柱和四项必需实验，但具体数值结果尚未给出（待后续报告）。现有数据支持了假设1（分数雅可比连续性）。

## 一句话评价
首次从理论上定位了扩散语音增强模型中噪声功率失配引起的kink现象，提供了精确的路径变分流分析方法。

---

## 17. Suppressing spectral edge effects in Schroeder Harmonic Complex

**作者**: Alessandro Altoè
**链接**: [2606.23847](https://arxiv.org/abs/2606.23847)
**分类**: Auditory Stimuli Design | **关键词**: Schroeder harmonic complex, tapered Schroeder complex, FM sweep, spectral edge effects, group delay, low crest factor

## 总结

**核心痛点**：传统Schroeder谐波复音（Schroeder's harmonic complex）在频带边缘存在稳态频率固定成分，易被听者察觉，干扰行为实验解释；周期调频扫描（periodic FM sweep）虽没有稳态成分，但每个周期起始处存在宽带点击成分。

**方法创新**：提出“渐缩Schroeder复音”（tapered Schroeder complex），通过扩展频带并在频带外施加渐缩函数（指数衰减，阶数M控制衰减斜率），同时保持频带内幅度平坦。相位仍采用Schroeder原始相位公式（式2），从而保留线性调频特性并抑制边缘效应。

**实验结果**：与Schroeder复音和周期FM扫描相比，渐缩Schroeder复音的频谱图无明显的水平（稳态）或垂直（点击）线条，仅有轻微边缘拖尾。听觉测试表明稳态成分和点击感被显著抑制。

**一句话评价**：简单有效的频谱边缘平滑方法，解决了听觉研究中长期存在的刺激伪迹问题。

---

## 18. Heterogeneous 2D/1D Signal Representation Fusion for Underwater Acoustic Modulation Recognition Under Distribution Shift

**作者**: Ronglai Qian, Liang An, Xiaoyan Wang, Qing Fan, Ziwei Huang, Yang Ye
**链接**: [2606.23702](https://arxiv.org/abs/2606.23702)
**分类**: Underwater Acoustic Modulation Recognition | **关键词**: underwater acoustic modulation recognition, distribution shift, heterogeneous signal representation fusion, cross-attention, benchmark dataset, UAMR-ShiftBench, SCP-TriCA

## 核心痛点
水下声学调制识别面临分布偏移（低SNR、未见过环境、未见过通信参数、仿真到实测）时，异构信号表示（2D时频图/循环平稳图与1D高阶功率谱）的不均匀退化导致融合鲁棒性差。现有评估缺乏统一协议，不同偏移类型混在一起，难以归因；现有融合方法对称处理所有模态，无法抑制退化模态的影响。

## 方法创新
1. **UAMR-ShiftBench基准**：首个统一评估协议，覆盖分布内、低SNR、未见过环境、未见过通信参数、实测海试（两次独立南海试验）五种条件，实现偏移解耦。
2. **SCP-TriCA融合框架**：分层三模态融合。第一阶段：STFT与循环平稳图（2D）通过双向交叉注意力对齐，得到统一2D表示；第二阶段：该表示通过交叉注意力查询1D统计特征（P2/P4功率谱），并用样本自适应选通门控制1D信息的注入量，避免不可靠模态的干扰。

## 实验结果
- 在UAMR-ShiftBench上，分布内准确率95.33%，模拟OOD平均74.59%，超越最强基线5.12个百分点。
- 在两次海试子集上分别达91.14%和94.86%，超越最强基线15.71和23.00个百分点。
- 消融实验验证了模态互补性和分层融合设计的增益。

## 一句话评价
首个系统解决水下声学调制识别中分布偏移下异构表示融合鲁棒性的工作，兼顾基准与模型创新。

---

## 19. Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching Speech Enhancement

**作者**: Wangyi Pu, Michele Scarpiniti
**链接**: [2606.24745](https://arxiv.org/abs/2606.24745)
**分类**: Audio Enhancement | **关键词**: Speech Enhancement, Flow Matching, Latent Representation Alignment, Skip-Free Backbone, Descript Audio Codec, Generative Model

## 核心痛点
U-Net跳跃连接虽保留精细声学细节，但可能传递噪声相关的低级特征，增加解码器负担；扩散/得分模型迭代采样步数多，限制实时部署。

## 方法创新
提出无跳跃连接的编码器-解码器骨干，用于流匹配（Flow Matching）语音增强。通过潜在表示对齐（LRA），利用冻结的Descript Audio Codec（DAC，去除残差向量量化）提取干净语音潜在特征，监督瓶颈和解码器表示。采用x预测参数化、FiLM时间嵌入、多周期/多分辨率判别器。

## 实验结果
在WSJ0-CHiME3和VoiceBank-DEMAND上评估，仅5次函数评估。相比U-Net基线，LRA在VB-DMD上PESQ从2.88提升至3.11，DNSMOS、WVMOS等感知指标最佳；WSJ0-CHiME3上PESQ略有提升。对抗训练改善感知质量但略微降低SI-SDR。

## 一句话评价
该方法通过无跳跃连接架构与DAC潜在对齐，有效抑制噪声泄露，在保持高效推理的同时提升感知质量。

---

## 20. CN-NewsTTS Bench: a target-level automatic benchmark for raw-input Chinese news TTS pronunciation

**作者**: Shijun Luo
**链接**: [2606.24714](https://arxiv.org/abs/2606.24714)
**分类**: Text-to-Speech | **关键词**: Chinese news TTS, pronunciation benchmark, text normalization, ASR-based evaluation, raw-input, target-level evaluation

# CN-NewsTTS Bench: 中文新闻TTS发音自动基准

## 核心痛点
- 中文新闻文本中包含密集的书面形式（如分数、型号、范围、单位符号、百分比、英文缩写、中英混合名称等），现有TTS系统常读错，且主观评测或通用ASR回环评测无法精准捕捉这些特定目标。
- 用户端无法使用规则、LLM重写、SSML提示或手动编辑来纠正，需要评估系统对原始输入的直接发音能力。

## 方法创新
- **原始输入产品赛道**：固定原始文本输入，禁止外部规则/LLM/SSML/手动编辑，评估TTS产品端到端行为。
- **目标级标注**：每个记录包含目标片段（span）、类型、正读（positive）和误读（negative）模式，支持自动评估。
- **三ASR自动评分协议**：使用MiMo API ASR、SenseVoiceSmall、Paraformer-zh三个异构ASR，多数投票决定目标正确/错误/未知。主要指标为严格准确率（StrictAcc = 正确数/可评估目标总数）。
- **公开数据集**：200条开发集、800条公开测试集，共1260个目标（含992个可自动评估目标），来自11个模板家族和86个词条，确定性生成。

## 实验结果
- 在7个商业TTS系统（Volcano/Doubao、Azure、Google、MiniMax、Aliyun、MiMo、AWS Polly）上评估。
- 最佳系统（Volcano）严格准确率0.879，覆盖率达0.913；多个系统低于0.60。
- 类别难度差异大：百分比、车辆型号、缩写几乎完美；体育比分最难（平均准确率0.233），主要误读为将连词符读成范围而非比分。
- ASR消融实验显示双ASR子集（Paraformer+SenseVoice）稳定性高，仅改变1.27%标签。

## 一句话评价
首个针对中文新闻TTS原始输入发音的自动化、可复现基准，揭示了商业系统在密集书面形式上的显著性能差距。

---

## 21. ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge

**作者**: Jisu Jeon, Seungyeon Jwa, Joosung Lee, Jinhyeon Kim, Woojin Chung, Hwiyeol Jo, Jeonghoon Kim, Jonghyun Choi, Soyoon Kim
**链接**: [2606.24648](https://arxiv.org/abs/2606.24648)
**分类**: Speech Generation Evaluation | **关键词**: Paralinguistic Assessment, Pairwise Comparison, LALM-as-a-Judge, Audio Benchmark, Speech Evaluation

## 论文总结

### 核心痛点
当前LALM（大型音频语言模型）在评估生成语音时主要关注整体自然度，忽略了副语言学细粒度特征（如语速、强调、风格等），且存在严重的校准失败（尤其在Tie情况下无法正确弃权）。

### 方法创新
提出了**PARAPairaudioBench**，一个包含5,175个音频对的成对基准测试，覆盖5个副语言学维度：Style、Rate、Emphasis、Age、Gender。设计包括：（1）诊断性多维度评估，分解副语言判断为五个标准；（2）显式Tie条件，评估模型在模糊情况下的弃权能力；（3）文本控制，通过相同/不同文本条件分离词汇与声学依赖。

### 实验结果
- 当前LALM judge平均落后人类32个百分点（人类79.2% vs. 最佳模型61.5%）。
- 模型在Rate（全局时序线索）上表现较好（最高88.9%），但在Emphasis（局部韵律）上表现差（最高49.7%）。
- Tie准确率极低（如GPT-4o Audio在Style Tie上仅3.8%），校准失败严重。
- 位置偏差高达29.4个百分点。
- 模型在Style上过度依赖文本线索，在Emphasis上忽视韵律上下文。

### 一句话评价
**PARAPairaudioBench揭示了当前LALM-as-a-Judge在细粒度副语言评估上的系统缺陷，为未来模型改进提供了诊断性基准。**

---

## 22. VieSpeaker: A Large-Scale Vietnamese Speaker Recognition Dataset Beyond Visual Dependency

**作者**: Viet Hoang Pham, Tran Trung Nguyen, Bao Thu Ho, Phuong Tuan Dat, Thi Thu Trang Nguyen
**链接**: [2606.24066](https://arxiv.org/abs/2606.24066)
**分类**: Speaker Recognition | **关键词**: Vietnamese speaker recognition, large-scale dataset, LLM-based speaker identification, face-independent pipeline, speaker diarization

## 核心痛点
越南语说话人识别面临数据资源匮乏，现有数据集（如Vietnam-Celeb、VoxVietnam）规模小、声学多样性不足，且大多依赖人脸信息进行身份标注，限制了数据来源（如无法包含仅音频的播客、电话录音等），增加了数据采集成本和标注质量对图像条件的敏感性。

## 方法创新
提出一种不依赖视觉模态的数据集构建流程：1）数据收集：从YouTube手动筛选采访、娱乐、播客三类频道的播放列表，获取音频和文本元数据（标题、描述、字幕）。2）说话人分割：使用Pyannote的speaker-diarization-3.1模型进行说话人日志化，生成匿名说话人ID和时间戳。3）说话人识别：利用LLM（Gemini 2.5 Pro）结合视频元数据和逐句样本，基于结构化提示推断真实身份，输出JSON映射及证据。4）说话人合并：对同一说话人跨视频的身份进行规范化（去前缀、标准化），并采用基于ECAPA-TDNN嵌入的余弦相似度聚类（阈值0.7合并，0.2分离），辅以人工验证。5）数据清洗：去除异常段（基于IQR的余弦相似度）、短于1秒的段、总时长低于30秒的说话人，并对主导说话人（如主持人）进行下采样以平衡分布。

## 实验结果
构建的VieSpeaker数据集包含365,874个话语、4,715个说话人，总计902.03小时，是迄今最大且最全面的越南语说话人识别数据集。实验采用ECAPA-TDNN架构，在WeSpeaker框架上训练。与仅用Vietnam-Celeb或VoxVietnam的基线相比，VieSpeaker训练的模型在评估集上表现出更好的鲁棒性和泛化能力，尤其在跨域场景下。数据集划分包含4000个说话人的训练集（VieSpeaker-T）和715个说话人的评估集（分为Easy和Hard两个协议）。

## 一句话评价
VieSpeaker通过创新的无视觉依赖管道，显著扩大了越南语说话人识别数据集规模，为低资源语言的数据构建提供了新方向。

---

## 23. Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks

**作者**: Taiyu Meng, Wenbin Jiang, Haoyi Zhang, Yuhan Zhou, Haibing Yin
**链接**: [2606.23761](https://arxiv.org/abs/2606.23761)
**分类**: Audio Enhancement | **关键词**: speech enhancement, spiking neural networks, neuromorphic, dual-branch, parameter efficiency

## 核心痛点
传统基于ANN的语音增强模型参数量大、计算成本高，难以部署在低功耗边缘设备上。现有SNN方法性能不如ANN，且通常只建模单一频谱维度，未能充分利用幅度谱和复数谱的互补优势。

## 方法创新
提出GSU-DBNet，一种双分支SNN架构，包含编码器-分离器-解码器。分离器中采用双路径门控脉冲单元（GSU）：频率路径使用双向BiGSU捕获全局频谱相关性，时间路径使用单向GSU进行因果时序建模。解码器双分支分别估计复数掩码（通过DeepFilter进行相位感知重建）和幅度掩码，然后加权融合。使用门控脉冲单元（GSU），仅含遗忘门，参数为LSTM的一半。

## 实验结果
在VoiceBank+DEMAND数据集上，GSU-DBNet以394K参数达到PESQ 3.04，CSIG 4.28，CBAK 3.57，COVL 3.68，SSNR 9.94。参数仅为代表性ANN模型的4.5%-10.6%，PESQ比DPSNN高0.84，比Spiking-FSN高0.38。

## 一句话评价
GSU-DBNet以极少的参数实现了与先进ANN模型相当的语音增强性能，展现了SNN在低功耗场景下的潜力。

---

