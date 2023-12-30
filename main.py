from flask import Flask, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'

@app.route('/')
def index():

    return getPosition(-1, -1)

@app.route('/<x>/<y>')
def getPosition(x, y):

    global arrBbox

    #TODO: Get Streaming Video

    #TODO: Predict and get bounding boxes
    bbox_pred = {"id": 0, "position":(0, 0, 100, 100), "hidden": False}
    arrBbox.append(bbox) #Append if bbox is new

    chosen_bboxes = []
    for bbox in arrBbox:

        x0, y0, x1, y1 = bbox["position"]

        #Determine if mouse click is in the bounding box
        if (x - x0) * (x - x1) <= 0 and (y - y0) * (y - y1) <= 0:
            chosen_bboxes.append(bbox["id"])

    #Find most possible bbox to show/hide
    mnd = 0x3f3f3f3f
    mni = -1
    for bid in chosen_bboxes:

        x0, y0, x1, y1 = bbox["position"]

        d = x - x0 + y - y0 #Manhathan distance
        if d < mnd:
            mnd = d
            mni = bid
    
    for bbox in arrBbox:
        if bbox["id"] == mni:
            bbox["hidden"] = not bbox["hidden"]
            break

    
    #TODO: Draw bbox if hidden is False
    
    #TODO: return streamed output
    
    return render_template('./index.html', clickX = x, clickY = y) #For debug

if __name__ == '__main__':

    global arrBbox
    arrBbox = []

    app.run('0.0.0.0')
