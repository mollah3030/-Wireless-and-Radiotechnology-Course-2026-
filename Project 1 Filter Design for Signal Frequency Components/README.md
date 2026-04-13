# Filter Design Assignment

## Student Information
- **Name:** [Your Name]
- **Student ID:** [Your Student ID]

## Objective
The goal of this assignment is to design suitable filters to isolate specific frequency components from a composite input signal.

## Input Signal
The input signal is the sum of four sine waves:

**Input Signal = A₁·sin(2π·100·t) + A₂·sin(2π·200·t) + A₃·sin(2π·300·t) + A₄·sin(2π·400·t)**

The frequency components present in the signal are:

- 100 Hz
- 200 Hz
- 300 Hz
- 400 Hz

## Filter Selection Table

| Frequency Component | Filter Type | Cutoff Frequency / Frequencies |
|---------------------|-------------|--------------------------------|
| 100 Hz | Low Pass Filter (LPF) | 150 Hz |
| 400 Hz | High Pass Filter (HPF) | 350 Hz |
| 100 Hz and 200 Hz | Low Pass Filter (LPF) | 250 Hz |
| 200 Hz | Band Pass Filter (BPF) | 190 Hz to 210 Hz |
| 300 Hz | Band Pass Filter (BPF) | 290 Hz to 310 Hz |
| 300 Hz and 400 Hz | High Pass Filter (HPF) | 250 Hz |
| 200 Hz and 300 Hz | Band Pass Filter (BPF) | 150 Hz to 350 Hz |
| 200 Hz, 300 Hz, and 400 Hz | High Pass Filter (HPF) | 150 Hz |
| 100 Hz and 400 Hz | Band Stop Filter (BSF) | Stopband: 150 Hz to 350 Hz |

## Explanation

### 1. 100 Hz
A Low Pass Filter with a cutoff at 150 Hz will pass the 100 Hz component and block the higher frequency components. This makes it suitable for isolating the lowest frequency in the signal.

### 2. 400 Hz
A High Pass Filter with a cutoff at 350 Hz will allow the 400 Hz component to pass while rejecting the lower frequencies. This is a suitable choice for isolating the highest frequency component.

### 3. 100 Hz and 200 Hz
A Low Pass Filter with a cutoff at 250 Hz will pass both 100 Hz and 200 Hz while blocking 300 Hz and 400 Hz. This helps isolate the two lower-frequency components together.

### 4. 200 Hz
A Band Pass Filter with a range from 190 Hz to 210 Hz will isolate the 200 Hz component. This narrow range helps reduce the influence of nearby frequencies.

### 5. 300 Hz
A Band Pass Filter with a range from 290 Hz to 310 Hz will isolate the 300 Hz component. This makes it possible to select the target frequency more accurately.

### 6. 300 Hz and 400 Hz
A High Pass Filter with a cutoff at 250 Hz will pass both 300 Hz and 400 Hz while rejecting 100 Hz and 200 Hz. This is a simple way to isolate the higher-frequency group.

### 7. 200 Hz and 300 Hz
A Band Pass Filter with cutoff frequencies from 150 Hz to 350 Hz will allow 200 Hz and 300 Hz to pass. At the same time, it blocks the 100 Hz and 400 Hz components.

### 8. 200 Hz, 300 Hz, and 400 Hz
A High Pass Filter with a cutoff at 150 Hz will pass 200 Hz, 300 Hz, and 400 Hz. It blocks the 100 Hz component, leaving the three higher frequencies.

### 9. 100 Hz and 400 Hz
A Band Stop Filter with a stopband from 150 Hz to 350 Hz will remove the middle frequencies, 200 Hz and 300 Hz. As a result, the 100 Hz and 400 Hz components remain.

## Conclusion
In this assignment, different filter types were selected based on the frequency components that needed to be isolated. Low Pass, High Pass, Band Pass, and Band Stop filters can all be used depending on whether low, high, middle, or separated frequency ranges are required.
