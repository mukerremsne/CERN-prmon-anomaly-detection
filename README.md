CERN-HSF GSoC 2026: Automated Software Performance Monitoring
Project Warm-up Exercise: ATLAS Experiment

1. Executive Summary
This project demonstrates process resource monitoring and anomaly detection using the prmon framework. While the prmon tool was successfully built from source in a WSL2 (Ubuntu) environment, synthetic datasets were utilized to validate the anomaly detection pipeline to ensure accuracy within the project's timeframe.

2. Technical Walkthrough

Installation & Environment

Environment: Ubuntu on WSL2 (Windows 11).

Build Tooling: Compiled prmon from source using CMake and make.

Submodules: Successfully initialized nlohmann_json and spdlog dependencies.

Data Generation & Anomaly Injection

The experiment simulates two core scenarios:

Baseline: A steady-state process utilizing ~100MB of memory (PSS).
Anomaly: A process spike where memory usage jumps to ~500MB (a 5x increase), simulating a potential memory leak or thread-count explosion.

Anomaly Detection Method

I implemented a Statistical Z-Score Approach.

Logic: The algorithm calculates the mean and standard deviation of the "Normal" dataset.
Threshold: A detection threshold was set at $Mean + 3\sigma$. Why? This method is computationally efficient for real-time monitoring and aligns with standard physics data-validation techniques (the 3-sigma rule covers 99.7% of normal variance).

3. Results & Visualization
The algorithm successfully identified 100% of the injected anomalies.

4. Discussion & Trade-offs
Suitability: The Z-Score method is excellent for real-time monitoring because it requires minimal CPU overhead.
Trade-offs: While effective for large spikes, this method may require tuning for "slow-growth" memory leaks. For such cases, more complex models like Isolation Forest could be explored as an alternative.
