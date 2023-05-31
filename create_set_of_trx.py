trx_sample = {
  "amount": 500.00,
  "description": "Monthly Rent",
  "direction": "Outgoing",
  "counterparty": "XYZ Property Management",
  "current": "1234567890",
  "transaction_type": "Electronic Transfer",
  "date": "2023-05-31",
  "payment_reference": "RNT202305",
  "currency": "USD",
  "payment_method": "Bank Transfer",
  "status": "Pending",
  "processing_fee": 5.00,
  "sender_name": "John Doe",
  "sender_account": "987654321",
  "recipient_name": "Jane Smith",
  "recipient_account": "543216789",
  "memo": "Payment for May rent",
  "authorization_code": "ABCDE12345",
  "routing_number": "123456789",
  "batch_id": "BATCH202305"
}

print([trx_sample] * 25)
