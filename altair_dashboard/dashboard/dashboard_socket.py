# import tornado

# class EchoWebSocket(tornado.websocket.WebSocketHandler):
#     def open(self):
#         print("WebSocket opened")

#     def on_message(self, message):
#         self.write_message(u"You said: " + message)

#     def on_close(self):
#         print("WebSocket closed")