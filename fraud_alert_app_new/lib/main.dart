import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'sms_receiver.dart';


void main() {
  runApp(FraudAlertApp());
}

class FraudAlertApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Cyber Fraud Alert Assistant',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: FraudCheckScreen(),
    );
  }
}

class FraudCheckScreen extends StatefulWidget {
  @override
  _FraudCheckScreenState createState() => _FraudCheckScreenState();
}

class _FraudCheckScreenState extends State<FraudCheckScreen> {
  final TextEditingController _controller = TextEditingController();
  String _result = '';
  bool _isLoading = false;
  
  @override
  void initState() {
    super.initState();
    SmsReceiver().listenForSms((msg) {
      print("Received SMS: $msg");
      setState(() {
        _controller.text = msg;
      });
      _checkFraud(); // Automatically checks when new SMS is received
    });
  }

  Future<void> _checkFraud() async {
    setState(() {
      _isLoading = true;
      _result = '';
    });

    final message = _controller.text;
    final uri = Uri.parse('https://fraud-api-0lkm.onrender.com/predict'); // Replace this with your actual deployed API URL

    try {
      final response = await http.post(
        uri,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'message': message}),
      );

      if (response.statusCode == 200) {
        final json = jsonDecode(response.body);
        setState(() {
          _result = json['result'].contains('🚨 Scam') ? '🚨 Scam Detected!' : '✅ Looks Legit';
        });
      } else {
        setState(() {
          _result = '❌ API Error: ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _result = '⚠️ Failed to connect to API.\n$e';
      });
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Cyber Fraud Alert Assistant'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              maxLines: 4,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Paste a suspicious message or transcript here...',
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: _isLoading ? null : _checkFraud,
              child: Text(_isLoading ? 'Checking...' : 'Check for Scam'),
            ),
            SizedBox(height: 24),
            if (_result.isNotEmpty)
              Text(
                _result,
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: _result.contains('Scam') ? Colors.red : Colors.green,
                ),
              ),
          ],
        ),
      ),
    );
  }
}
