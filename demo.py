# import pywhatkit

# phone_number = "+919708591482"  # Receiver ka number
# message = "Hello! This message is sent using Python."

# # 7:45 AM par message schedule karenge
# hour = 7
# minute = 45

# pywhatkit.sendwhatmsg(
#     phone_number,
#     message,
#     hour,
#     minute
# )

# print("WhatsApp message scheduled!")



import pywhatkit

# Normal text ko handwriting mein convert karna
pywhatkit.text_to_handwriting(
    "Hello bhai! I am learning Python.",
    save_to="handwriting.png"
)

print("Handwriting image created successfully!")
