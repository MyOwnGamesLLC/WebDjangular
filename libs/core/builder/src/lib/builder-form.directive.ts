import {
  ComponentFactoryResolver,
  ComponentRef,
  Directive,
  Input,
  OnChanges,
  OnInit,
  Type,
  ViewContainerRef,
  Output,
  EventEmitter,
  SimpleChanges
} from '@angular/core';
import { FormGroup } from '@angular/forms';
import { BuilderFormButtonComponent } from './inputs/button/button.component';
import { BuilderFormInputComponent } from './inputs/input/input.component';
import { BuilderFormSelectComponent } from './inputs/select/select.component';
import { BuilderFormNgSelectComponent } from './inputs/ngselect/ngselect.component';
import { BuilderFormCodeComponent } from './inputs/code/code.component';
import { BuilderFormBuilderComponent } from './inputs/form_builder/form_builder.component';
import { BuilderFormArrayComponent } from './inputs/form_array/form-array.component';
import { BuilderFormSwitcherComponent } from './inputs/switch/switch.component';
import { BuilderFormGroupComponent } from './inputs/form_group/form_group.component';
import { BuilderFormCheckboxComponent } from './inputs/checkbox/checkbox.component';
import { BuilderFormDatepickerComponent } from './inputs/datepicker/datepicker.component';
import { BuilderFormJsonLogicComponent } from './inputs/json_logic/json_logic.component';
import {
  BuilderFormField,
  BuilderFormFieldConfig
} from './interfaces/form-config.interface';
import { BuilderFormTextAreaComponent } from './inputs/textarea/textarea.component';
import { BuilderFormLabelComponent } from './inputs/label/label.component';
import { BuilderFormRelationshipCheckboxOptionsComponent } from './inputs/relationship_checkbox/checkbox.component';

const components: { [type: string]: Type<BuilderFormField> } = {
  button: BuilderFormButtonComponent,
  text: BuilderFormInputComponent,
  textArea: BuilderFormTextAreaComponent,
  select: BuilderFormSelectComponent,
  ngSelect: BuilderFormNgSelectComponent,
  codeEditor: BuilderFormCodeComponent,
  formBuilder: BuilderFormBuilderComponent,
  formArray: BuilderFormArrayComponent,
  formGroup: BuilderFormGroupComponent,
  switch: BuilderFormSwitcherComponent,
  relationship_checkbox: BuilderFormRelationshipCheckboxOptionsComponent,
  checkbox: BuilderFormCheckboxComponent,
  datepicker: BuilderFormDatepickerComponent,
  jsonLogic: BuilderFormJsonLogicComponent,
  label: BuilderFormLabelComponent,
};

@Directive({
  selector: '[wdaBuilderFormFields]'
})
export class ScaffoldFieldDirective implements BuilderFormField, OnChanges, OnInit {
  @Input() config: BuilderFormFieldConfig;
  @Input() group: FormGroup;
  @Output() relationshipUpdated: EventEmitter<any> = new EventEmitter();

  component: ComponentRef<BuilderFormField>;

  constructor(
    private resolver: ComponentFactoryResolver,
    private container: ViewContainerRef
  ) { }

  ngOnChanges(changes: SimpleChanges) {
    if (!changes.config.isFirstChange()) {
      if (this.component) {
        this.component.instance.config = this.config;
        this.component.instance.group = this.group;
        this.component.instance.relationshipUpdated = this.relationshipUpdated;
      }
    }
  }

  ngOnInit() {
    if (this.config.type === 'hidden') return;
    if (!components[this.config.type]) {
      const supportedTypes = Object.keys(components).join(', ');
      throw new Error(
        `Trying to use an unsupported type (${this.config.type}).
        Supported types: ${supportedTypes}`
      );
    }
    const component = this.resolver.resolveComponentFactory<BuilderFormField>(
      components[this.config.type]
    );
    this.component = this.container.createComponent(component);
    this.component.instance.config = this.config;
    this.component.instance.group = this.group;
    this.component.instance.relationshipUpdated = this.relationshipUpdated;
  }
}
