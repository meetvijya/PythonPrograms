using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    interface IBuilder
    {
        void DoIt();
        string GetProductName { get; }
    }
}
