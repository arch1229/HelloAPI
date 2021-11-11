from device_registry import app

print('Hello Docker Python=3.4 !')

print('~ Running Flask Server ~')

app.run(host='0.0.0.0', port=80, debug=True)
