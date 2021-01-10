import com.espertech.esper.common.client.EPCompiled;
import com.espertech.esper.common.client.configuration.Configuration;
import com.espertech.esper.compiler.client.CompilerArguments;
import com.espertech.esper.compiler.client.EPCompileException;
import com.espertech.esper.compiler.client.EPCompilerProvider;
import com.espertech.esper.runtime.client.*;


public class AppCoder {
    public static void main(String[] args) throws InterruptedException {

        Configuration configuration = new Configuration();
        configuration.getCommon().addEventType("EventCoder", EventCoder.class);

        //指定事件模型
        String coderModel = EventCoder.class.getName();

        //描述复杂事件
        String epl = "select name,salary,age from " + coderModel;

        EPCompiled compiled;
        try {
            CompilerArguments compilerArguments = new CompilerArguments(configuration);
            compiled = EPCompilerProvider.getCompiler().compile(epl, compilerArguments);

            EPRuntime runtime = EPRuntimeProvider.getDefaultRuntime(configuration);
            EPDeployment deployment;
            try {
                deployment = runtime.getDeploymentService().deploy(compiled);

                deployment.getStatements()[0].addListener(new ListenerCoder());

                //模拟事件发生
                for (int i = 0; i < 10; i++) {
                    EventCoder eventCoder = new EventCoder();
                    eventCoder.setName("coder"+i);
                    eventCoder.setAge(20+i);
                    runtime.getEventService().sendEventBean(eventCoder, "EventCoder");
                }

            } catch (EPDeployException e) {
                e.printStackTrace();
            }

        } catch (EPCompileException e) {
            e.printStackTrace();
        }

    }
}