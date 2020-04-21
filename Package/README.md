# getClassifyRes_exe

此文件夹为打包后的exe可执行文件，将这个文件夹下的文件都放到debug目录下并创建名为temp和highMass的文件夹，以下是c# winform调用的例子。

```c#
            //Debug目录下建立temp和highMass文件夹
            string wav = @"fileway";//传进音频绝对路径
            ProcessStartInfo myStartInfo = new ProcessStartInfo();
            myStartInfo.FileName = Application.StartupPath + @"\__init__.exe";
            myStartInfo.Arguments = wav;
            myStartInfo.UseShellExecute = false;//不打开控制台窗口
            myStartInfo.CreateNoWindow = true;// 不打开控制台窗口
            myStartInfo.RedirectStandardOutput = true;//输出参数设定
            Process myProcess = new Process();
            myProcess.StartInfo = myStartInfo;

            myProcess.Start();
            string output = myProcess.StandardOutput.ReadToEnd();
            myProcess.WaitForExit();
            txtres.Text = output;
```



# Merge_exe

目录文件夹下需要有temp文件夹里面存放分割的音频，是需要和getClassifyRes配合使用的。

```python
# sys[1]-分类列表，sys[2]-合并结果路径，包括新音频命名
Merge(sys.argv[1].split(), sys.argv[2])
```

由于控制台只接受字符串形式，所以需要将接受的字符串转化为数组，即运行该可执行文件的命令为`Merge.exe "person person person person person person person person person" "res.wav"`。

c# winform调用同理，有多个接收参数的情况下，Arguments中多个参数用空格隔开。



# cleanup_exe

将同级目录下的highMass和temp里面的文件清空，可以在载入文件前执行此脚本。



# cutWavByUser_exe

传进四个参数，第一个参数是接受处理音频的路径，第二个是开始秒数，第三个是结束时间，第四个是保存的路径。
c# 调用

```c#
            //切割
            ProcessStartInfo myStartInfo = new ProcessStartInfo();
            myStartInfo.FileName = Application.StartupPath + @"\cutwav.exe";
            myStartInfo.Arguments = "F:/code/Audio_classification/dataBase/UrbanSound8K_byclass/person/A2_1.wav " +
                "2 8 F:/code/Audio_classification/stupid.wav";
            myStartInfo.UseShellExecute = false;//不打开控制台窗口
            myStartInfo.CreateNoWindow = true;// 不打开控制台窗口
            myStartInfo.RedirectStandardOutput = false;//输出参数设定
            Process myProcess = new Process();
            myProcess.StartInfo = myStartInfo;

            myProcess.Start();
            myProcess.WaitForExit();
```

