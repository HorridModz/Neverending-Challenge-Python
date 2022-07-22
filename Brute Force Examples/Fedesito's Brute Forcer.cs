var txtFiles = Directory.EnumerateFiles("./", 
                                        "*", SearchOption.AllDirectories)
               .Where(s => s.EndsWith("This.txt"))
               .ToList();
for (int i = 0; i < txtFiles.Count; i++)
{
    string[] arraytest = txtFiles.ToArray();
    string result = File.ReadAllText(arraytest[i]);
    if (!result.Contains("RIP BOZO"))
    {
        Console.WriteLine("found at " + arraytest[i]);
    }
}
