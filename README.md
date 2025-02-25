# Apple Detect AI System

![Webcap photo](https://raw.githubusercontent.com/techn0man1ac/AppleDetectAISystem/refs/heads/main/imgs/filename.jpg)

Apple Detect AI System is a simple AI-powered system that detects apples using a camera and controls an Arduino board based on the detection result. This project uses **LM Studio** to run the **MiniCPM V-2.6** multimodal AI model locally.

## How It Works

1. The **camera** captures an image.
2. The image is **sent to the AI model** ([MiniCPM V-2.6](https://huggingface.co/openbmb/MiniCPM-V-2_6) running on [LM Studio](https://lmstudio.ai/)).
3. The AI **analyzes the image** and determines if an apple is present.
4. If an apple is detected:
   - The system sends `1` to the Arduino board.
   - The Arduino turns **on an LED** (or another connected device).
5. If no apple is detected:
   - The system sends `0` to the Arduino board.
   - The Arduino turns **off the LED**.

## Requirements

### Hardware

- **Computer** (to run LM Studio and process images)
- **Camera** (compatible with `pygame.camera`)
- **Arduino Board** (e.g., Arduino Uno)
- **LED or other output device**
- **USB cable** (to connect the Arduino)

### Software

- **Python 3**
- **LM Studio** (running MiniCPM V-2.6)
- **Arduino IDE**
- Python Libraries:
  - `openai`
  - `pygame`
  - `pyserial`

## Installation & Setup

### 1. Set Up LM Studio

- Download and install **LM Studio**.
- Load the **MiniCPM V-2.6** model.
- Start the LM Studio server (`http://localhost:1234/v1`).

### 2. Install Python Dependencies

```sh
pip install openai pygame pyserial
```

### 3. Upload Arduino Code

- Open `SaAIDS.ino` in the **Arduino IDE**.
- Select the correct **board** and **port**.
- Upload the code to the Arduino.

### 4. Run the Python Script

```sh
python CVTestAI.py
```

## Expected Output

- If an apple is detected: **LED turns on**.
- If no apple is detected: **LED remains off**.
- The console prints: `Yes` or `No`.

## License

This project is licensed under the **[MIT License](https://github.com/techn0man1ac/AppleDetectAISystem/blob/main/LICENSE)**.

