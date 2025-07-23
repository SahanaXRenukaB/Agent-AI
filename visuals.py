# Optional: Generate a chart using matplotlib and return base64 image
import matplotlib.pyplot as plt
import io
import base64

def generate_chart(df, x, y):
    fig, ax = plt.subplots()
    df.plot(kind='bar', x=x, y=y, ax=ax)
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    return base64.b64encode(buf.getvalue()).decode('utf-8')
