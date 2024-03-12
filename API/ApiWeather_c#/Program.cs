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
using Newtonsoft.Json;

namespace ConsoleApp6
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("welcome to app weather :) ");
            Console.WriteLine("**************************** ");
            Console.WriteLine("please enter the name city:");

            string city = Console.ReadLine();
            var client = new RestClient();
            var url = $"https://api.weatherbit.io/v2.0/forecast/daily?&city={city}&key=2effe1f9f06e40cc8ef77eb5be376022";
            var request = new RestRequest(url, Method.Get);
            RestResponse response = client.Get(request);
             JObject s = JObject.Parse(response);
            string yourPrompt = (string)s["dialog"]["prompt"];


            Console.ReadKey();

            
           
            /*RestResponse response = await client.ExecuteAsync(request);*/

        }
    }
}
