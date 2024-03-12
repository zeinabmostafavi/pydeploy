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
            Console.WriteLine("welcome :) ");
            Console.WriteLine("**************************** ");
            Console.WriteLine("please enter the name fruit:");

            string fruit = Console.ReadLine();
            var client = new RestClient();
            var url = $"https://fruityvice.com/api/fruit/{fruit}";
            var request = new RestRequest(url, Method.Get);
            RestResponse response = client.Get(request);
            JObject s = JObject.Parse(response.Content);
            string yourPrompt = (string)s["name"];


            Console.ReadKey();

            
           
            /*RestResponse response = await client.ExecuteAsync(request);*/

        }
    }
}
