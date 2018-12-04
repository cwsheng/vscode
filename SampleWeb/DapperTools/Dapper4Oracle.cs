using System;

namespace DapperTools
{
    public class Dapper4Oracle
    {
        public Dapper4Oracle()
        {
            Oracle.ManagedDataAccess.Client.OracleConnection conn = new Oracle.ManagedDataAccess.Client.OracleConnection ();
        }
    }
}
