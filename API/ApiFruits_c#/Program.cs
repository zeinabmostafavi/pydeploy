using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using RestSharp;
using Newtonsoft.Json.Linq;

namespace ConsoleApp6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("welcome  :) ");
            Console.WriteLine("**************************** ");
            Console.WriteLine("please enter the name fruite:");
            string name_fruite = Console.ReadLine();

            var client = new RestClient();
            var url = $"https://fruityvice.com/api/fruit/{name_fruite}";
            var request = new RestRequest(url, Method.Get);
            RestResponse response = client.Get(request);
            Console.WriteLine(response.content);
            JObject data = JObject.Parse(response);
            string namr = (string)data["name"];
            string suger = (string)data["nutritions"]["suger"];
            string calories = (string)data["nutritions"]["calories"];
            string carbohydrates = (string)data["nutritions"]["carbohydrates"];
            string protein = (string)data["nutritions"]["protein"];
            Console.WriteLine($"name:\t{name_fruite} suger:{suger} carbohydrates:{carbohydrates} calories:/t{calories}");

            Console.ReadKey();



            /*RestResponse response = await client.ExecuteAsync(request);*/

        }
    }
}
