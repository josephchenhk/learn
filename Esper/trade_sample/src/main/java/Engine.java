import com.espertech.esper.common.client.EPCompiled;
import com.espertech.esper.common.client.configuration.Configuration;
import com.espertech.esper.compiler.client.CompilerArguments;
import com.espertech.esper.compiler.client.EPCompileException;
import com.espertech.esper.compiler.client.EPCompilerProvider;
import com.espertech.esper.runtime.client.*;
import com.opencsv.exceptions.CsvException;

import java.io.IOException;
import java.util.Arrays;

public class Engine {

    static String[] rowData;
    static String timeStr;
    static java.sql.Timestamp ts;
    static String company;
    static Double px;

    static EPCompiled compiled;
    static EPDeployment deployment;

    public static void main(String[] args) throws IOException, CsvException, EPCompileException, EPDeployException {
        System.out.println("Test Esper Engine");

        Configuration configuration = new Configuration();
        configuration.getCommon().addEventType("Event", Event.class);
        //指定事件模型
        String coderModel = Event.class.getName();
        //描述复杂事件
        String epl = "select ts,company,px from " + coderModel;

        CompilerArguments compilerArguments = new CompilerArguments(configuration);
        compiled = EPCompilerProvider.getCompiler().compile(epl, compilerArguments);
        EPRuntime runtime = EPRuntimeProvider.getDefaultRuntime(configuration);
//        deployment = runtime.getDeploymentService().deploy(compiled);
//        deployment.getStatements()[0].addListener(new Listener());
        deployment = runtime.getDeploymentService().deploy(compiled, new DeploymentOptions().setDeploymentId("test-deployment"));
        runtime.getDeploymentService().getStatement("test-deployment","alert").addListener(new Listener());

        String fileName = "/Users/joseph/Dropbox/code/learn/Q/table.csv";

        DataReader dr = new DataReader(fileName);

        // dr.r.forEach(x -> System.out.println(Arrays.toString(x)));

        for(int i=1; i<dr.r.size(); i++){
            rowData = dr.r.get(i);
            timeStr = rowData[0];
            company = rowData[1];
            px = Double.valueOf(rowData[2]);
//            System.out.println(ts + ";" + company + ";" + px);
            ts = java.sql.Timestamp.valueOf("2021-01-04 "+timeStr) ;
            Event event = new Event(ts, company, px);

//            System.out.println(event);
            runtime.getEventService().sendEventBean(event, "Event");
        }
    }
}
