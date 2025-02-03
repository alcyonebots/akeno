from Emilia.custom_filter import register
from Emilia.utils.decorators import *
import speedtest
import matplotlib.pyplot as plt
import io
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Registering the /speedtest command
@register(pattern="/speedtest")
@rate_limit(3, 60)
async def speedtest_command(event):
    # Initialize speedtest with Ookla's Speedtest
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    # Prepare the text result
    text_result = f"🔹 **Download Speed**: {download_speed:.2f} Mbps\n"
    text_result += f"🔹 **Upload Speed**: {upload_speed:.2f} Mbps\n"
    text_result += f"🔹 **Ping**: {ping} ms"

    # Prepare the image result (Speed test graph)
    fig, ax = plt.subplots()
    ax.bar(["Download", "Upload"], [download_speed, upload_speed], color=["blue", "orange"])
    ax.set_title("Speedtest Results")
    ax.set_ylabel("Speed (Mbps)")
    ax.set_ylim(0, max(download_speed, upload_speed) + 5)

    # Save the plot as a BytesIO object
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format="PNG")
    image_stream.seek(0)

    # Inline buttons for choosing result format
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Text Result", callback_data="text_result"),
         InlineKeyboardButton("Image Result", callback_data="image_result")]
    ])

    # Send a message with inline buttons for user to choose
    await event.reply(
        "Speed Test Results: Choose the format to view the result.",
        reply_markup=buttons
    )

    # Store the results temporarily in the event for further processing
    event.data = {
        "text_result": text_result,
        "image_stream": image_stream
    }


# Handler for the inline button callback
@register(pattern="callback")
async def handle_callback(event):
    data = event.data
    if data == "text_result":
        # Send text result
        await event.reply(data["text_result"])
    elif data == "image_result":
        # Send image result
        await event.reply_photo(photo=data["image_stream"])
