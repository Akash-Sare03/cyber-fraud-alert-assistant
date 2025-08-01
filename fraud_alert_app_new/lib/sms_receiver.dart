import 'package:telephony/telephony.dart';

class SmsReceiver {
  final Telephony telephony = Telephony.instance;

  void listenForSms(Function(String) onMessageReceived) async {
    bool? permissionsGranted = await telephony.requestPhoneAndSmsPermissions;

    if (permissionsGranted ?? false) {
      telephony.listenIncomingSms(
        onNewMessage: (SmsMessage message) {
          try {
            if (message.body != null) {
              onMessageReceived(message.body!);
            }
          } catch (e) {
            print("Error in SMS callback: $e");
          }
        },
        onBackgroundMessage: _backgroundMessageHandler, // ← use with underscore
      );
    } else {
      print("SMS permissions not granted.");
    }
  }
}

// ✅ Define background handler outside the class, with underscore
void _backgroundMessageHandler(SmsMessage message) {
  print("Background SMS: ${message.body}");
}
