using System;
using Newtonsoft.Json;

namespace HelloDotNet
{
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var person = new Person { Name = "Alice", Age = 30 };
            string json = JsonConvert.SerializeObject(person);

            Console.WriteLine("Serialized JSON:");
            Console.WriteLine(json);
        }
    }
}
