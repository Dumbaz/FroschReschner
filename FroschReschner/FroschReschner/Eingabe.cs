using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FroschReschner
{
    public partial class Eingabe: Component
    {    
        public Eingabe()
        {
            InitializeComponent();
        }

        public Eingabe(IContainer container)
        {
            container.Add(this);

            InitializeComponent();
        }
    }
}
