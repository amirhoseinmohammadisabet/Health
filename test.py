import matplotlib.pyplot as plt

# First ECG data
ecg_data_1 = [-0.11252183, -2.8272038, -3.7738969, -4.3497511, -4.376041, -3.4749863, -2.1814082, -1.8182865,
              -1.2505219, -0.47749208, -0.36380791, -0.49195659, -0.42185509, -0.30920086, -0.4959387, -0.34211867,
              -0.35533627, -0.36791303, -0.31650279, -0.41237405, -0.47167181, -0.41345783, -0.36461703, -0.44929829,
              -0.47141866, -0.42477658, -0.46251673, -0.55247236, -0.47537519, -0.6942, -0.7018681, -0.59381178,
              -0.66068415, -0.71383066, -0.76980688, -0.67228161, -0.65367605, -0.63940562, -0.55930228, -0.59167032,
              -0.49322332, -0.46305183, -0.30164382, -0.23273401, -0.12505488, -0.15394314, -0.024357404, -0.065608758,
              0.034999258, 0.061935219, 0.07119542, 0.12392505, 0.10312371, 0.22522849, 0.12868305, 0.30248315, 0.25727621,
              0.19635161, 0.17938297, 0.24472863, 0.34121687, 0.32820441, 0.40604169, 0.44660507, 0.42406823, 0.48151204,
              0.4778438, 0.62408259, 0.57458456, 0.59801319, 0.5645919, 0.607979, 0.62063457, 0.65625291, 0.68474806,
              0.69427284, 0.66558377, 0.57579577, 0.63813479, 0.61491695, 0.56908343, 0.46857572, 0.44281777, 0.46827436,
              0.43249295, 0.40795792, 0.41862256, 0.36253075, 0.41095901, 0.47166633, 0.37216676, 0.33787543, 0.22140511,
              0.27399747, 0.29866408, 0.26356357, 0.34256352, 0.41950529, 0.58660736, 0.86062387, 1.1733446, 1.2581791,
              1.4337887, 1.7005334, 1.9990431, 2.1253411, 1.9932907, 1.9322463, 1.7974367, 1.5222839, 1.2511679, 0.99873034,
              0.48372242, 0.023132292, -0.19491383, -0.22091729, -0.24373668, -0.25469462, -0.29113555, -0.25649034,
              -0.22787425, -0.32242276, -0.28928586, -0.31816951, -0.36365359, -0.39345584, -0.26641886, -0.25682316,
              -0.28869399, -0.16233755, 0.16034772, 0.79216787, 0.93354122, 0.79695779, 0.57862066, 0.2577399, 0.22807718,
              0.12343082, 0.92528624, 0.19313742]

# Plotting the ECG data
plt.figure(figsize=(12, 6))
plt.plot(ecg_data_1)
plt.title('ECG Data - Patient 1')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()
