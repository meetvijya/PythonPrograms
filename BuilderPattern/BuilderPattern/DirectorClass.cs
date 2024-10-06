using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuilderPattern
{
    class DirectorClass
    {
        IBuilder _build = null;

        public void Construct(IBuilder build)
        {
            build.DoIt();
        }
    }
}
