import java.sql.*;

public class MySQLConnectTest {
    private static Connection dbTest;
    private String id = "one";
    private String password = "one111";

    MySQLConnectTest() {
        connectDB();
    }

    private void connectDB() {
        try {
            // JDBC Driver Loading
            Class.forName("org.mariadb.jdbc.Driver").newInstance();
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/", id, password);
            System.out.println("Connect to mySQL");
        }catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Failed to connect to mySQL");
            System.out.println("SQLException:"+e);
        }catch (Exception e) {
            System.out.println("Exception:"+e);
        }
    }

    public static void main(String[] args) {
        new MySQLConnectTest();
//        try {
//            dbTest.close();
//        }catch (SQLException e) {
//            e.printStackTrace();
//            System.out.println("SQLException:"+e);
//        }
    }
}
