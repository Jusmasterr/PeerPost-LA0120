using System.Diagnostics;

class Program
{
    private static Process hostProcess = null;
    private static Process clientProcess = null;


    public static void Main(string[] args)
    {
        while (true)
        {

            Console.WriteLine("Wählen Sie den Modus:");
            Console.WriteLine("1. Host starten");
            Console.WriteLine("2. Client starten");
            Console.WriteLine("3. Beenden");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    StartHost();
                    break;
                case "2":
                    RunClient();
                    break;
                case "3":
                    StopProcesses();
                    return;
                default:
                    Console.WriteLine("Ungültige Auswahl. Bitte wählen Sie erneut.");
                    break;
            }
        }
    }


    private static void StartHost()
    {

        string scriptPath = "\"C:\\Users\\LucaJ\\source\\repos\\Peer2Peer\\Host.py\"";

        ProcessStartInfo start = new ProcessStartInfo
        {
            FileName = "python",
            Arguments = $"\"{scriptPath}\"",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            CreateNoWindow = true
        };

        try
        {

            if (hostProcess == null || hostProcess.HasExited)
            {
                hostProcess = Process.Start(start);
                Console.WriteLine("Host gestartet. Läuft im Hintergrund.");
            }
            else
            {
                Console.WriteLine("Der Host ist bereits ausgeführt.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Fehler beim Starten des Hosts: {ex.Message}");
        }
    }


    private static void RunClient()
    {
        string scriptPath = "\"C:\\Users\\LucaJ\\source\\repos\\Peer2Peer\\client.py\"";

        ProcessStartInfo start = new ProcessStartInfo
        {
            FileName = "python",
            Arguments = $"\"{scriptPath}\"",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            CreateNoWindow = false
        };

        try
        {

            if (clientProcess == null || clientProcess.HasExited)
            {
                clientProcess = Process.Start(start);
                Console.WriteLine("Client gestartet. Sie können Nachrichten senden und Dateien übertragen.");
            }
            else
            {
                Console.WriteLine("Der Client ist bereits ausgeführt.");
            }


            using (StreamReader reader = clientProcess.StandardOutput)
            {
                string output = reader.ReadToEnd();
                Console.WriteLine("Client Output:");
                Console.WriteLine(output);
            }


            using (StreamReader errorReader = clientProcess.StandardError)
            {
                string error = errorReader.ReadToEnd();
                if (!string.IsNullOrEmpty(error))
                {
                    Console.WriteLine("Client Errors:");
                    Console.WriteLine(error);
                }
            }

            clientProcess.WaitForExit();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Fehler beim Ausführen des Clients: {ex.Message}");
        }
    }


    private static void StopProcesses()
    {
        try
        {
            if (hostProcess != null && !hostProcess.HasExited)
            {
                hostProcess.Kill();
                Console.WriteLine("Host wurde gestoppt.");
            }

            if (clientProcess != null && !clientProcess.HasExited)
            {
                clientProcess.Kill();
                Console.WriteLine("Client wurde gestoppt.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Fehler beim Stoppen der Prozesse: {ex.Message}");
        }
    }
}
