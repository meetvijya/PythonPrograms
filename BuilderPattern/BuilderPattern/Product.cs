using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    class Product
    {
        string productname = string.Empty;
        public Product(string productname)
        {
            this.productname = productname;
        }

        public string GetProductName()
        {
            return ("Product name is:" + productname);
        }
    }
}
