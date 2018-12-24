using System;                           /* Exception */
using System.Collections;
using System.IO;
using System.Text;
using System.Net.Sockets;
using UnityEngine;

#if !UNITY_EDITOR
using System.Threading.Tasks;
using Windows.Foundation.Diagnostics;
#endif

public class NetworkClient : MonoBehaviour
{
    public string host = "192.168.43.112";
    public Int32 port = 5050;
    private StreamWriter socket_writer;
    private StreamReader socket_reader;
    private string received_data;

#if !UNITY_EDITOR
    private Task exchangeTask;
    private Windows.Networking.Sockets.StreamSocket socket;
#endif    
    void Start()
    {
#if !UNITY_EDITOR
        Connect();
#endif
        InvokeRepeating("my_coroutine", 1.0f, 1.0f);
    }
    public void Connect()
    {
#if !UNITY_EDITOR
        ConnectUWP(host, port.ToString());
#endif
    }

#if !UNITY_EDITOR
    private async void ConnectUWP(string host, string port)
    {
            try
            {   
                if (exchangeTask != null) StopExchange();            
                socket = new Windows.Networking.Sockets.StreamSocket();
                Windows.Networking.HostName serverHost = new Windows.Networking.HostName(host);                
                await socket.ConnectAsync(serverHost, port);
                Stream streamOut = socket.OutputStream.AsStreamForWrite();
                socket_writer = new StreamWriter(streamOut) { AutoFlush = true };
                Stream streamIn = socket.InputStream.AsStreamForRead();
                socket_reader = new StreamReader(streamIn);
            }
            catch (Exception e)
            {
                Debug.Log(e.ToString());
            }
    }
#endif

    public void StopExchange()
    {
#if !UNITY_EDITOR
        if (exchangeTask != null)
        {
            exchangeTask.Wait();
            socket.Dispose();
            socket_writer.Dispose();
            socket_reader.Dispose();
            socket = null;
            exchangeTask = null;
            socket_writer = null;
            socket_reader = null;
        }
#endif
    }

    void my_coroutine()
    {   

    }

    void OnSelect()
    {
        socket_writer.WriteLine("gesture_tap");
    }

    private void OnApplicationQuit()
    {
        StopExchange();
    }
}
