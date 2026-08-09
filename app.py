from ultralytics import YOLO
import gradio as gr


# Load YOLO model
model = YOLO("model/best (2).pt")


# Image detection
def detect_image(image, confidence):
    if image is None:
        return None

    results = model.predict(
        source=image,
        conf=confidence,
        verbose=False
    )

    result = results[0]

    # Draw bounding boxes
    annotated_image = result.plot()

    return annotated_image


# Live webcam detection
def detect_webcam(image, confidence):
    if image is None:
        return None

    results = model.predict(
        source=image,
        conf=confidence,
        verbose=False
    )

    result = results[0]

    annotated_image = result.plot()

    return annotated_image


# -----------------------------
# Gradio Interface
# -----------------------------

with gr.Blocks(title="Rock Paper Scissors YOLO") as demo:

    gr.Markdown(
        """
        # ✊ Rock Paper Scissors Detection
        ### YOLO Object Detection
        """
    )

    confidence = gr.Slider(
        minimum=0.1,
        maximum=1.0,
        value=0.5,
        step=0.05,
        label="Confidence Threshold"
    )

    with gr.Tabs():

        # =========================
        # Upload Image
        # =========================

        with gr.Tab("📁 Upload Image"):

            input_image = gr.Image(
                type="numpy",
                label="Upload Image"
            )

            detect_button = gr.Button(
                "🔍 Detect",
                variant="primary"
            )

            output_image = gr.Image(
                label="Detection Result"
            )

            detect_button.click(
                fn=detect_image,
                inputs=[
                    input_image,
                    confidence
                ],
                outputs=output_image
            )

        # =========================
        # Live Webcam
        # =========================

        with gr.Tab("📷 Live Camera"):

            webcam = gr.Image(
                sources=["webcam"],
                type="numpy",
                streaming=True,
                label="Webcam"
            )

            webcam_output = gr.Image(
                label="Live Detection"
            )

            webcam.stream(
                fn=detect_webcam,
                inputs=[
                    webcam,
                    confidence
                ],
                outputs=webcam_output
            )


# Launch
demo.launch()