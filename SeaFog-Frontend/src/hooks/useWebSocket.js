import { ref } from 'vue';
import { Client } from '@stomp/stompjs';
import SockJS from 'sockjs-client';

const useWebSocket = () => {
  const stompClient = ref(null);
  let messageCallback = null;
  const connectionStatus = ref('disconnected');
  const fileProgress = new Map();
  let totalFiles = 0;

  const connect = (sessionId, callback) => {
    try {
      const wsUrl = '/dev-api/ws';
      console.log('Connecting to WebSocket URL:', wsUrl);

      const socket = new SockJS(wsUrl);

      socket.onopen = () => {
        console.log('SockJS connection opened');
        connectionStatus.value = 'connecting';
      };

      socket.onclose = (event) => {
        console.log('SockJS connection closed:', event);
        connectionStatus.value = 'disconnected';
      };

      socket.onerror = (error) => {
        console.error('SockJS error:', error);
        connectionStatus.value = 'error';
      };

      stompClient.value = new Client({
        webSocketFactory: () => socket,
        debug: function(str) {
          console.log('STOMP Debug:', str);
        },
        reconnectDelay: 5000,
        heartbeatIncoming: 4000,
        heartbeatOutgoing: 4000,
        onConnect: function() {
          console.log('STOMP Connected');
          connectionStatus.value = 'connected';
          
          this.subscribe(`/topic/progress/${sessionId}`, (message) => {
            try {
              console.log('Received message:', message.body);
              const data = JSON.parse(message.body);
              
              if (data.totalFiles) {
                totalFiles = data.totalFiles;
                console.log('Total files to process:', totalFiles);
              }

              if (data.fileId) {
                fileProgress.set(data.fileId, data.progress || 0);
              }

              if (totalFiles > 0) {
                const totalProgress = Array.from(fileProgress.values()).reduce((sum, progress) => sum + progress, 0) / totalFiles;
                
                if (messageCallback) {
                  messageCallback({
                    ...data,
                    progress: Math.round(totalProgress),
                    totalFiles: totalFiles,
                    currentFile: fileProgress.size
                  });
                }
              } else {
                if (messageCallback) {
                  messageCallback(data);
                }
              }
            } catch (error) {
              console.error('Error processing message:', error);
              handleError('消息处理失败', error);
            }
          });
        },
        onStompError: function(frame) {
          console.error('STOMP error:', frame);
          handleError('STOMP 协议错误', frame);
        },
        onDisconnect: function() {
          console.log('STOMP Disconnected');
          connectionStatus.value = 'disconnected';
          fileProgress.clear();
          totalFiles = 0;
        }
      });

      messageCallback = callback;
      console.log('Activating STOMP client...');
      stompClient.value.activate();

    } catch (error) {
      console.error('Error creating WebSocket:', error);
      handleError('WebSocket 创建失败', error);
    }
  };

  const handleError = (message, error) => {
    console.error(message, error);
    connectionStatus.value = 'error';
    if (messageCallback) {
      messageCallback({
        progress: 0,
        message: `${message}: ${error.message || '未知错误'}`,
        status: 'FAILED'
      });
    }
  };

  const disconnect = () => {
    if (stompClient.value) {
      console.log('Disconnecting STOMP client...');
      try {
        stompClient.value.deactivate();
        stompClient.value = null;
        messageCallback = null;
        connectionStatus.value = 'disconnected';
      } catch (error) {
        console.error('Error disconnecting:', error);
        handleError('断开连接失败', error);
      }
    }
  };

  return {
    connect,
    disconnect,
    connectionStatus
  };
};

export default useWebSocket;