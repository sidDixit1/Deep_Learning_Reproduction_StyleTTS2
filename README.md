# Reproduction of StyleTTS 2 in French
### Siddharth Dixit, Javier Alonso Garcia, Louis Bruninx, Thomas van de Pavoordt

#### Based on [StyleTTS 2](https://github.com/yl4579/StyleTTS2) by Yinghao Aaron Li, Cong Han, Vinay S. Raghavan, Gavin Mischler, Nima Mesgarani

> The purpose of this repo is to reproduce the results of the paper "StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models" in French. This is done for the Deep Learning course (CS4240) at TU Delft.

**Blog post:** [https://lflbruninx.github.io/DeepLearningBlog/](https://lflbruninx.github.io/DeepLearningBlog/)

## Pre-requisites
1. Python >= 3.7
2. Clone this repository:
```bash
git clone https://github.com/sidDixit1/Deep_Learning_Reproduction_StyleTTS2.git
cd Deep_Learning_Reproduction_StyleTTS2
```
3. Install python requirements: 
```bash
pip install -r requirements.txt
```
On Windows add:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 -U
```
Also install phonemizer and espeak if you want to run the demo:
```bash
pip install phonemizer
sudo apt-get install espeak-ng
```
4. Download a French dataset. For example: [here](https://datashare.ed.ac.uk/handle/10283/2353). Unzip and convert the sample rate to 24kHz. If changing the dataset, make sure to change the lists in "Data" accordingly with phoneme information.

## Training
1. Make sure to configure the `config_ft_fr.yml` file with correct paths, and to maximize the capabilities of your machine.
2. Run the finetuning training script with either:
```bash
python train_finetune.py --config_path ./Configs/config_ft_fr.yml
```
or, if using a single GPU, you may accelerate training with
```bash
accelerate launch --mixed_precision=fp16 --num_processes=1 train_finetune_accelerate.py --config_path ./Configs/config_ft.yml
```

For reference, training to 30 epochs took about 100 hours with an Nvidia L4 GPU.

## Inference
Use the python notebook in "Demo/Inference_french.ipynb" to generate audio samples from the trained model. If using other notebooks, make sure to use the multilingual PL-BERT, and set the phonemizer to the correct language.

## Troubleshooting
If you encounter any issues, it may be useful to refer to the README and issues of the original repository: [https://github.com/yl4579/StyleTTS2](https://github.com/yl4579/StyleTTS2)