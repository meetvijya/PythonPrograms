using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    class Program
    {
        static void Main(string[] args)
        {
            IBuilder _build = null;
            DirectorClass d = new DirectorClass();
            _build = new BuilderA();

            d.Construct(_build);
            Console.WriteLine(_build.GetProductName);

            _build = new BuilderB();

            d.Construct(_build);
            Console.WriteLine(_build.GetProductName);
            Console.ReadKey();
        }
    }
}
