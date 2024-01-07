from kafka import KafkaConsumer


def create_consumer():
    return KafkaConsumer(
        'create-accounts-result-json-topic',  # Thay thế bằng tên topic của bạn
        bootstrap_servers=['localhost:9092'],  # Thay thế bằng địa chỉ của Kafka broker của bạn
        auto_offset_reset='earliest',  # Bắt đầu consume từ earliest message
        group_id='my_consumer_group'  # Thay thế bằng consumer group của bạn nếu cần
    )

def consume_messages(consumer):
    for message in consumer:
        print(f"Received message: {message.value}")

if __name__ == '__main__':
    kafka_consumer = create_consumer()
    consume_messages(kafka_consumer)