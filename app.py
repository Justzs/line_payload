from flask import Flask, json, jsonify, request

app = Flask(__name__)

# img_url = ""
# display_name = ""
# place = ""
# work_time = ""
# contact = ""
# website = ""

def create_flex_template(img_url, display_name, place, work_time, contact, website):
    line_template = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": img_url,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "postback",
                "label": "action",
                "data": "contact"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": display_name,
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Place",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "text",
                                    "text": place,
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Time",
                                    "color": "#aaaaaa",
                                    "size": "sm",
                                    "flex": 1
                                },
                                {
                                    "type": "text",
                                    "text": work_time,
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "sm",
                                    "flex": 5
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "postback",
                                "label": "CONTACT",
                                "data": contact
                            }
                        }
                    ],
                    "margin": "sm"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "uri",
                                "label": "WEBSITE",
                                "uri": website
                            }
                        }
                    ]
                }
            ],
            "flex": 0
        }
    }
    return line_template


def createFlex(bubble_json):
    lineresult = {
        "type": "flex",
        "altText": "This is a flex message",
        "contents": [bubble_json]
    }

    payload = {
        "response_type": "object",
        "line_payload": [lineresult]
    }

    return payload


@app.route('/')
def index():
    return "Hello botnoi"


@app.route('/id_card')
def id_card():
    img_url = request.args.get('img_url')
    display_name = request.args.get('display_name')
    place = request.args.get('place')
    work_time = request.args.get('work_time')
    contact = request.args.get('contact')
    website = request.args.get('website')

    flex_message = create_flex_template(img_url, display_name, place, work_time, contact, website)

    payload = createFlex(flex_message)
    return jsonify(payload)


if __name__ == '__main__':
    app.run(debug=True)