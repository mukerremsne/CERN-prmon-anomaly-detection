CERN-HSF GSoC 2026: Automated Software Performance Monitoring
Project Warm-up Exercise: ATLAS Experiment

Overview

This exercise explores process resource monitoring and anomaly detection using time-series data similar to metrics produced by prmon.

prmon was built from source in a WSL2 (Ubuntu) environment.  
To test the anomaly detection pipeline within the project timeframe, synthetic datasets were generated that simulate normal and abnormal memory usage.

Environment Setup

System: Ubuntu (WSL2 on Windows 11)

prmon was compiled from source using CMake and make.

Required submodules were initialized:
- nlohmann_json
- spdlog

Dataset Generation

Two datasets were generated:

Normal workload  
- Process memory (PSS) around ~100 MB  
- Small random fluctuations added to simulate noise

Anomalous workload  
- Memory spike to ~500 MB between timestamps 30–45  
- Represents abnormal behaviour such as a memory leak or excessive thread usage

Anomaly Detection Method

A statistical Z-score threshold was used.

The mean and standard deviation were calculated from the normal dataset:

threshold = mean + 3 × standard deviation

Any PSS value exceeding this threshold was classified as an anomaly.

The 3-sigma rule covers ~99.7% of normal variance and provides a simple,
low-overhead method suitable for real-time monitoring.

Results

The detection algorithm successfully flagged the injected anomaly region
between timestamps 30–45.

The resulting plot shows:
- normal baseline behaviour (~100 MB (~100,000 KB))
- the anomaly threshold
- detected anomaly points

Discussion

Advantages
- Very low computational cost
- Easy to interpret
- Suitable for real-time monitoring

Limitations
- Less effective for gradual memory growth
- Assumes relatively stable baseline behaviour

More advanced anomaly detection methods (e.g. Isolation Forest from scikit-learn)
could improve detection of subtle or slow-growing anomalies.

This exercise demonstrates a simple anomaly detection pipeline
for monitoring process memory usage. The statistical threshold
method successfully identified the injected anomaly and provides
a lightweight baseline approach for software performance monitoring.
